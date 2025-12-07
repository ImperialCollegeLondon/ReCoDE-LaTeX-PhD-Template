import re
from pathlib import Path

input_file = "phd-thesis/chapters/04-results.tex"
output_file = "docs/4_Explanation_Figures.md"

SNIPPET_NAMES = ["figures_four", "figures_two"]

def extract_snippet(tex_lines, name):
    start_marker = f"% START SNIPPET: {name}"
    end_marker   = f"% END SNIPPET: {name}"

    inside_block = False
    lines = []

    for line in tex_lines:
        if start_marker in line:
            inside_block = True
            continue
        if end_marker in line:
            inside_block = False
            break
        if inside_block:
            lines.append(line)

    return "\n".join(lines)

def main():
    tex_path = Path(input_file)
    md_path = Path(output_file)

    if not tex_path.is_file():
        raise FileNotFoundError(f"Tex file not found: {tex_path}")
    if not md_path.is_file():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    tex_lines = tex_path.read_text(encoding="utf-8").splitlines()
    snippet = extract_snippet(tex_lines, SNIPPET_NAME)

    if not snippet.strip():
        print(f"[WARN] No snippet found for '{SNIPPET_NAME}'")
        return

    print(f"[INFO] Snippet '{SNIPPET_NAME}' length: {len(snippet)} characters")

    md_content = md_path.read_text(encoding="utf-8")

    # 1. Try to replace an existing block:
    # <!-- SNIPPET: figures -->
    # ```latex
    #...
    # ```
    pattern_block = re.compile(
        r"(<!-- SNIPPET: figures -->\s*)```latex.*?```",
        re.DOTALL,
    )

    # ✅ Use a function so backslashes in `snippet` are not interpreted
    def repl_block(match):
        prefix = match.group(1)  # the "<!-- SNIPPET... -->" + any whitespace
        return f"{prefix}```latex\n{snippet}\n```"

    new_md_content, replaced_count = pattern_block.subn(repl_block, md_content)

    if replaced_count == 0:
        print("[WARN] No existing snippet block found – inserting a new one after the marker.")

        marker = "<!-- SNIPPET: figures -->"

        if marker not in md_content:
            print("[INFO] Marker not found; appending marker + block at end of file.")
            if not md_content.endswith("\n"):
                md_content += "\n"
            new_md_content = (
                md_content
                + "\n\n"
                + marker
                + "\n```latex\n"
                + snippet
                + "\n```"
            )
        else:
            # Insert a fresh block right after the marker
            new_md_content = md_content.replace(
                marker,
                marker + "\n```latex\n" + snippet + "\n```",
            )
    else:
        print(f"[INFO] Replaced {replaced_count} existing block(s).")

    md_path.write_text(new_md_content, encoding="utf-8")
    print(f"[DONE] Updated {output_file}")

if __name__ == "__main__":
    main()

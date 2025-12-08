import re
from pathlib import Path

# Adjust these if your files live elsewhere
input_file = "phd-thesis/chapters/03-methods.tex"
output_file = "docs/5_Equations.md"

SNIPPET_NAMES = ["equations_std", "equations_mean"]

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

def update_snippet_in_md(md_content, name, snippet):
    """
    Replace the block starting at:
      <!-- SNIPPET: {name} -->
    and the following ```latex... ``` with a fresh block using `snippet`.
    If no block is found, insert a new one after the marker.
    """
    marker = f"<!-- SNIPPET: {name} -->"

    # Pattern: marker + optional whitespace + ```latex... ```
    pattern_block = re.compile(
        rf"({re.escape(marker)}\s*)```latex.*?```",
        re.DOTALL,
    )

    def repl_block(match):
        prefix = match.group(1)  # marker + whitespace
        return f"{prefix}```latex\n{snippet}\n```"

    new_md_content, replaced_count = pattern_block.subn(repl_block, md_content)

    if replaced_count == 0:
        print(f"[WARN] No existing snippet block found for '{name}' – inserting a new one after the marker.")

        if marker not in md_content:
            print(f"[INFO] Marker '{marker}' not found; appending marker + block at end of file.")
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
            new_md_content = md_content.replace(
                marker,
                marker + "\n```latex\n" + snippet + "\n```",
            )
    else:
        print(f"[INFO] Updated block for '{name}' ({replaced_count} occurrence(s)).")

    return new_md_content

def main():
    tex_path = Path(input_file)
    md_path = Path(output_file)

    if not tex_path.is_file():
        raise FileNotFoundError(f"Tex file not found: {tex_path}")
    if not md_path.is_file():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    tex_lines = tex_path.read_text(encoding="utf-8").splitlines()
    md_content = md_path.read_text(encoding="utf-8")

    for name in SNIPPET_NAMES:
        snippet = extract_snippet(tex_lines, name)

        if not snippet.strip():
            print(f"[WARN] No snippet found for '{name}'")
            continue

        print(f"[INFO] Snippet '{name}' length: {len(snippet)} characters")

        md_content = update_snippet_in_md(md_content, name, snippet)

    md_path.write_text(md_content, encoding="utf-8")
    print(f"[DONE] Updated {output_file}")

if __name__ == "__main__":
    main()

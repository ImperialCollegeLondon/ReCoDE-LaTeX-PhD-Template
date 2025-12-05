import re
from pathlib import Path

input_file = "phd-thesis/preamble.tex"
output_file = "docs/2_Explanation_Preamble.md"

SNIPPET_NAME = "preamble"

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
    tex_lines = Path(input_file).read_text(encoding="utf-8").splitlines()
    snippet = extract_snippet(tex_lines, SNIPPET_NAME)

    if not snippet.strip():
        print(f"[WARN] No snippet found for '{SNIPPET_NAME}'")
        return

    print(f"[INFO] Snippet '{SNIPPET_NAME}' length: {len(snippet)}")

    md_path = Path(output_file)
    md_content = md_path.read_text(encoding="utf-8")

    placeholder = "<!-- SNIPPET: preamble -->"

    # 1. Remove any previously generated code block for this snippet
    #    Pattern: <!-- SNIPPET: preamble --> followed by ```latex... ```
    pattern_old_block = re.compile(
        r"<!-- SNIPPET: preamble -->\s*```latex.*?```",
        re.DOTALL
    )
    md_content, removed_count = re.subn(pattern_old_block, placeholder, md_content)
    if removed_count > 0:
        print(f"[INFO] Removed {removed_count} old generated block(s).")

    # 2. Ensure the placeholder exists somewhere (in case it was removed manually)
    if placeholder not in md_content:
        print("[INFO] Placeholder not found; appending it at the end of the file.")
        if not md_content.endswith("\n"):
            md_content += "\n"
        md_content += "\n" + placeholder + "\n"

    # 3. Replace the placeholder with the new code block (once)
    def repl(_match, snippet_text=snippet):
        return "```latex\n" + snippet_text + "\n```"

    pattern_placeholder = re.escape(placeholder)
    new_md_content, count = re.subn(pattern_placeholder, repl, md_content, count=1)

    if count == 0:
        print("[WARN] Placeholder replacement failed.")
    else:
        print("[INFO] Placeholder replaced with new snippet.")

    md_path.write_text(new_md_content, encoding="utf-8")
    print(f"[DONE] Updated {output_file}")

if __name__ == "__main__":
    main()

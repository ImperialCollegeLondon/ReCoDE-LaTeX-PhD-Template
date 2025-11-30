import re
from pathlib import Path

input_file = "phd-thesis/main.tex"                 # LaTeX source
output_file = "docs/Explanations/1_Explanation_Main.md"  # Destination Markdown

# List all snippet identifiers as used in main.tex and in the MD placeholders
SNIPPET_NAMES = [
    "documentclass",
    "preamble_title",
    "dedication",
    "Declaration of Originality",
    "Abstract",
    "Acknowledgements",
    "Dissemination",
    "Nomenclature_Acronyms",
    "Contents, List of Figures/Tables",
    "CHAPTERS",
    "APPENDIX",
    "Bibliography",
]

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

    snippet = "\n".join(lines)
    return snippet

def main():
    tex_lines = Path(input_file).read_text(encoding="utf-8").splitlines()
    md_path = Path(output_file)
    md_content = md_path.read_text(encoding="utf-8")

    for name in SNIPPET_NAMES:
        snippet = extract_snippet(tex_lines, name)
        if not snippet.strip():
            print(f"[WARN] No snippet found for '{name}'")
            continue

        print(f"[INFO] Snippet '{name}' length: {len(snippet)}")

        # Exact placeholder in the Markdown
        placeholder = f"<!-- SNIPPET: {name} -->"

        # Escape placeholder for regex search (handles spaces, commas, etc.)
        pattern = re.escape(placeholder)

        # Use a function as replacement so backslashes in LaTeX are NOT parsed
        def repl(_match, snippet_text=snippet):
            return "```latex\n" + snippet_text + "\n```"

        new_md_content, count = re.subn(pattern, repl, md_content)
        if count == 0:
            print(f"[WARN] Placeholder not found for '{name}'")
        else:
            print(f"[INFO] Replaced {count} occurrence(s) for '{name}'")

        md_content = new_md_content  # update for next snippet

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md_content, encoding="utf-8")
    print(f"[DONE] All snippets processed into {output_file}")

if __name__ == "__main__":
    main()

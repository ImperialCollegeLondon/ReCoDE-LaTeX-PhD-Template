# Purpose: Extract code between START/END markers in main.tex and update Markdown explanations.

import re
from pathlib import Path

# -------------------------------
# CONFIGURATION
# -------------------------------

input_file = "phd-thesis/main.tex"                # LaTeX source
output_file = "docs/Explanations/Testing.md"     # Destination Markdown
snippet_name = "documentclass"                    # Identifier in main.tex

start_marker = f"% START SNIPPET: {snippet_name}"
end_marker   = f"% END SNIPPET: {snippet_name}"

# -------------------------------
# READ LATEX FILE
# -------------------------------
tex_lines = Path(input_file).read_text(encoding="utf-8").splitlines()
snippet_lines = []
inside_block = False

for line in tex_lines:
    if start_marker in line:
        inside_block = True
        continue
    if end_marker in line:
        inside_block = False
        break  # stops after first matching snippet
    if inside_block:
        snippet_lines.append(line)

snippet = "\n".join(snippet_lines)

# -------------------------------
# READ MARKDOWN AND UPDATE
# -------------------------------
md_path = Path(output_file)
md_content = md_path.read_text(encoding="utf-8")

# Replace placeholder safely with literal LaTeX
updated_md = re.sub(
    r"<!-- SNIPPET: documentclass -->",
    lambda m: "```latex\n" + snippet + "\n```",
    md_content
)

# Write updated Markdown
md_path.parent.mkdir(parents=True, exist_ok=True)
md_path.write_text(updated_md, encoding="utf-8")

print(f"Snippet '{snippet_name}' inserted into {output_file}")


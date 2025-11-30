# File: Scripts/extract_snippet.py
# Purpose: Extract code between START/END markers in main.tex and update Markdown explanations.

import re

# -------------------------------
# CONFIGURATION
# -------------------------------
input_file = "phd-thesis/main.tex"                          # LaTeX source
output_file = "docs/Explanations/1_Explanation_Main.md"    # Destination Markdown
snippet_name = "documentclass"                              # Identifier in main.tex

# -------------------------------
# READ LaTeX FILE
# -------------------------------
with open(input_file, "r", encoding="utf-8") as f:
    tex_lines = f.readlines()

inside_block = False
snippet_lines = []

start_marker = f"% START SNIPPET: {snippet_name}"
end_marker = f"% END SNIPPET: {snippet_name}"

for line in tex_lines:
    if start_marker in line:
        inside_block = True
        continue
    if end_marker in line:
        inside_block = False
        break  # stops after first matching snippet
    if inside_block:
        snippet_lines.append(line)

# Format snippet as LaTeX code block
latex_block = "```latex\n" + "".join(snippet_lines) + "```\n"

# -------------------------------
# UPDATE MARKDOWN FILE
# -------------------------------
with open(output_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace the placeholder with the extracted snippet
updated_md = re.sub(
    r"```latex\s*<!-- SNIPPET WILL BE AUTO-INSERTED HERE -->\s*```",
    latex_block,
    md_content,
    count=1
)

# Write updated content back
with open(output_file, "w", encoding="utf-8") as f:
    f.write(updated_md)

print(f"Snippet '{snippet_name}' inserted into {output_file}")

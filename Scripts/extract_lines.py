# File: extract_snippet.py
# Purpose: Extract a LaTeX snippet from main.tex and insert it into a Markdown file

import re

# -----------------------------
# CONFIGURATION
# -----------------------------
tex_file = "phd-thesis/main.tex"                        # Your LaTeX source file
md_file  = "docs/Explanations/1_Explanation_Main.md"   # Your Markdown explanation file

snippet_name = "documentclass"  # The snippet name in your LaTeX file

start_marker = f"% START SNIPPET: {snippet_name}"
end_marker   = f"% END SNIPPET: {snippet_name}"

# -----------------------------
# READ LaTeX FILE
# -----------------------------
with open(tex_file, "r", encoding="utf-8") as f:
    tex_lines = f.readlines()

# Extract the snippet
inside = False
snippet_lines = []

for line in tex_lines:
    if start_marker in line:
        inside = True
        continue
    if end_marker in line and inside:
        inside = False
        break
    if inside:
        snippet_lines.append(line)

# Prepare the fenced LaTeX block
latex_block = "```latex\n" + "".join(snippet_lines) + "```\n"

# -----------------------------
# READ Markdown FILE
# -----------------------------
with open(md_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace the placeholder with the LaTeX snippet
placeholder_pattern = r"```latex\n<!-- SNIPPET WILL BE AUTO-INSERTED HERE -->\n```"
updated_md = re.sub(placeholder_pattern, latex_block, md_content, count=1)

# -----------------------------
# WRITE BACK UPDATED MARKDOWN
# -----------------------------
with open(md_file, "w", encoding="utf-8") as f:
    f.write(updated_md)

print(f"Snippet '{snippet_name}' inserted into {md_file}")


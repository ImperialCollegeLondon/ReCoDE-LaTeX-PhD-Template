# extract_snippet.py
import re

# -------------------------------
# CONFIGURATION
# -------------------------------
tex_file = "phd-thesis/main.tex"
md_file  = "docs/Explanations/1_Explanation_Main.md"

start_marker = "% START SNIPPET: documentclass"
end_marker   = "% END SNIPPET: documentclass"

# -------------------------------
# READ LaTeX FILE
# -------------------------------
with open(tex_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

inside_block = False
snippet_lines = []

for line in lines:
    if start_marker in line:
        inside_block = True
        continue
    if end_marker in line:
        inside_block = False
        break
    if inside_block:
        snippet_lines.append(line)

# -------------------------------
# READ MARKDOWN FILE
# -------------------------------
with open(md_file, "r", encoding="utf-8") as f:
    md_text = f.read()

# -------------------------------
# REPLACE PLACEHOLDER
# -------------------------------
latex_block = "```latex\n" + "".join(snippet_lines) + "```\n"

# Replace only the placeholder comment
md_text = re.sub(
    r"```latex\s*<!-- SNIPPET WILL BE AUTO-INSERTED HERE -->\s*```",
    latex_block,
    md_text
)

# -------------------------------
# WRITE UPDATED MARKDOWN
# -------------------------------
with open(md_file, "w", encoding="utf-8") as f:
    f.write(md_text)

print("Updated documentclass snippet in Markdown")

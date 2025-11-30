import os
import re

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

tex_file = "phd-thesis/main.tex"
explanation_file = "docs/Explanations/1_Explanation_Main.md"
snippet_name = "documentclass"

# ---------------------------------------------------
# EXTRACT SNIPPET
# ---------------------------------------------------

start_pattern = rf"% START SNIPPET:\s*{snippet_name}"
end_pattern   = rf"% END SNIPPET:\s*{snippet_name}"

with open(tex_file, "r") as f:
    lines = f.readlines()

inside = False
snippet = []

for line in lines:
    if re.search(start_pattern, line):
        inside = True
        continue
    if re.search(end_pattern, line) and inside:
        inside = False
        break
    if inside:
        snippet.append(line)

latex_block = "```latex\n" + "".join(snippet) + "```\n"

# ---------------------------------------------------
# UPDATE THE EXPLANATION MARKDOWN
# ---------------------------------------------------

with open(explanation_file, "r", encoding="utf-8") as f:
    md = f.read()

updated = re.sub(
    r"```latex[\s\S]*?```",
    latex_block,
    md,
    count=1
)

with open(explanation_file, "w", encoding="utf-8") as f:
    f.write(updated)

print(f"Updated snippet '{snippet_name}' inserted into {explanation_file}")

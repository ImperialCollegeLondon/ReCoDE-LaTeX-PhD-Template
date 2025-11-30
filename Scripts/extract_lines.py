import re

# -------------------------------
# CONFIGURATION
# -------------------------------
tex_file = "phd-thesis/main.tex"                     # LaTeX source file
md_file  = "docs/Explanations/1_Explanation_Main.md"  # Markdown destination

# -------------------------------
# READ LaTeX FILE
# -------------------------------
with open(tex_file, "r", encoding="utf-8") as f:
    tex_lines = f.readlines()

# -------------------------------
# EXTRACT ALL SNIPPETS
# -------------------------------
snippets = {}
snippet_name = None
snippet_lines = []

for line in tex_lines:
    start_match = re.match(r"% START SNIPPET: (.+)", line)
    end_match   = re.match(r"% END SNIPPET: (.+)", line)

    if start_match:
        snippet_name = start_match.group(1).strip()
        snippet_lines = []
        continue

    if end_match:
        end_name = end_match.group(1).strip()
        if snippet_name == end_name:
            snippets[snippet_name] = "".join(snippet_lines)
        snippet_name = None
        continue

    if snippet_name:
        snippet_lines.append(line)

# -------------------------------
# READ MARKDOWN FILE
# -------------------------------
with open(md_file, "r", encoding="utf-8") as f:
    md_text = f.read()

# -------------------------------
# REPLACE PLACEHOLDERS
# -------------------------------
def replace_placeholder(match):
    placeholder_name = match.group(1).strip()
    code = snippets.get(placeholder_name, "")
    return f"```latex\n{code}```"

md_text = re.sub(
    r"```latex\s*<!-- SNIPPET: (.+?) -->\s*```",
    replace_placeholder,
    md_text
)

# -------------------------------
# WRITE UPDATED MARKDOWN
# -------------------------------
with open(md_file, "w", encoding="utf-8") as f:
    f.write(md_text)

print("Markdown updated with snippets:", list(snippets.keys()))

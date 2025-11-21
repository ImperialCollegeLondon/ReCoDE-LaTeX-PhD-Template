# File: generate_include_snippet.py
# Purpose: Generate a Markdown snippet using mkdocs-include-markdown-plugin
#          instead of copying LaTeX lines manually.

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

# Path to your LaTeX source
input_file = "phd-thesis/main.tex"

# Output Markdown file
output_file = "Explanations/Testing.md"

# Markers inside the LaTeX file
start_marker = "% START SNIPPET"
end_marker   = "% END SNIPPET"

# ---------------------------------------------------
# SCRIPT
# ---------------------------------------------------

# Read lines
with open(input_file, "r") as f:
    lines = f.readlines()

# Find line numbers of the markers
start_line = None
end_line = None

for idx, line in enumerate(lines, start=1):
    if start_marker in line:
        start_line = idx + 1   # content starts AFTER marker
    if end_marker in line:
        end_line = idx - 1     # content ends BEFORE marker

# Safety check
if start_line is None or end_line is None:
    raise ValueError("Start or end marker not found in LaTeX file.")

# Write the INCLUDE directive instead of copying text
with open(output_file, "w") as f:
    f.write("```markdown\n")
    f.write(f":::include ../{input_file}\n")
    f.write(f"    start={start_line}\n")
    f.write(f"    end={end_line}\n")
    f.write("    code_language=latex\n")
    f.write("```\n")

print(f"Generated include snippet in {output_file}")


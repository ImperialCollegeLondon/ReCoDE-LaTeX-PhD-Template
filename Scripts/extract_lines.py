# File: extract_snippet.py
# Purpose: Copy the actual content between START/END markers
#          from a LaTeX file into a Markdown file.

# ---------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------

input_file = "phd-thesis/main.tex"      # LaTeX source
output_file = "docs/Explanations/1_Explanation_Main.md" # Destination

start_marker = "% START SNIPPET"
end_marker   = "% END SNIPPET"

# ---------------------------------------------------
# SCRIPT
# ---------------------------------------------------

with open(input_file, "r") as f:
    lines = f.readlines()

inside_block = False
snippet_lines = []

for line in lines:
    # Detect start marker
    if start_marker in line:
        inside_block = True
        continue  # skip the marker line itself

    # Detect end marker
    if end_marker in line:
        inside_block = False
        break  # stop after first block; remove if you want multiple blocks

    # Save lines inside block
    if inside_block:
        snippet_lines.append(line)

# Write to Markdown with fenced code block
with open(output_file, "w") as f:
    f.write("```latex\n")
    f.writelines(snippet_lines)
    f.write("```\n")

print(f"Extracted snippet written to {output_file}")


# File: extract_lines.py
# Purpose: Extract specific lines from a LaTeX file and generate a Markdown snippet.

# -------------------------------
# CONFIGURATION
# -------------------------------

# Path to your LaTeX file
input_file = "phd-thesis/main.tex"

# Path to the output Markdown file
output_file = "Explanations/Testing.md"

# Lines you want to include (start and end, inclusive)
start_line = 2
end_line = 10

# -------------------------------
# SCRIPT
# -------------------------------

# Read the LaTeX file
with open(input_file, "r") as f:
    lines = f.readlines()

# Select only the desired lines
selected_lines = lines[start_line - 1 : end_line]  # Python is 0-indexed

# Write the selected lines to the Markdown file with fenced code block
with open(output_file, "w") as f:
    f.write("```latex\n")          # Start of Markdown code block
    f.writelines(selected_lines)    # Write the selected lines
    f.write("\n```")                # End of Markdown code block

print(f"Lines {start_line}-{end_line} from {input_file} written to {output_file}")

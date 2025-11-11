## Preamble Explanation

The **preamble** in a LaTeX document is a section defined *before* `\begin{document}`that controls the **formatting, structure, typography, citation style, margins, and overall layout** of the entire thesis.

In this template, the preamble is configured to ensure:

✅ Compliance with **Imperial College Thesis Requirements** (Sections 4.1–4.6)  
✅ Correct margins and page layout as required by **Regulation 4.3**  
✅ Continuous Arabic numbering from the title page as required by **Regulation 4.4**  
✅ Professional typesetting of text, figures, tables, and mathematics  
✅ Clear, accessible PDF structure for electronic submission  
✅ A clean and modern academic style appropriate for engineering and design research  

Students normally do not need to modify the preamble, but understanding it helps ensure your thesis remains compliant and professionally formatted.

---

```latex
% --------------------------------------------------------------------
% Preamble: Packages and global formatting settings
% This template follows Imperial College Thesis Requirements (Sections 4.1–4.6).
% --------------------------------------------------------------------

% ------------------------------------------------------
% Character encoding and font setup
% ------------------------------------------------------
\usepackage[utf8]{inputenc}     % Ensures UTF-8 input encoding (recommended for modern documents).
\usepackage[T1]{fontenc}        % Provides proper T1 font encoding – improves hyphenation and PDF output.
\usepackage{lmodern}            % Latin Modern font family. Clear, scalable, and embedding-safe.

\usepackage{microtype}          % Improves kerning and character spacing throughout the thesis.
                                % Not required by Imperial, but considered excellent practice for readability.

% ------------------------------------------------------
% Mathematics and symbols
% ------------------------------------------------------
\usepackage{amsmath,amssymb}    % Standard AMS math packages – necessary for equations, symbols, alignments.

% ------------------------------------------------------
% Figures, graphics, captions
% ------------------------------------------------------
\usepackage{graphicx}           % Required for including images, diagrams, and plots.
\usepackage{caption}            % Provides better control of figure/table captions.
\usepackage{subcaption}         % Useful for multi-panel figures (Figure 1a, 1b, etc.).
                                % Allowed under Section 4.1: diagrams and illustrations must be clear.

% ------------------------------------------------------
% Hyperlinks and PDF structure
% ------------------------------------------------------
\usepackage{hyperref}           % Clickable references; improves examiner navigation in PDF.
\usepackage{bookmark}           % Ensures stable, well-structured PDF bookmarks.
                                % Strongly recommended for electronic submission (Section 4.1).

% ------------------------------------------------------
% Tables
% ------------------------------------------------------
\usepackage{booktabs}           % Professional-quality tables (\toprule, \midrule, \bottomrule).
                                % Good practice: improves readability; acceptable per Section 4.1.

% ------------------------------------------------------
% Page geometry (Regulations 4.3 and 4.4)
% ------------------------------------------------------
\usepackage{geometry}
\geometry{
  a4paper,
  inner=3cm,                    % Equal margins required (Regulation 4.3: page content centred).
  outer=3cm,
  top=3cm,
  bottom=3cm,
  heightrounded                 % Ensures consistent text height across pages.
}
                                % Imperial requires equal left/right margins (4.3) and continuous
                                % Arabic page numbering from the title page onward (4.4).
                                % These geometry settings enforce the margin requirement.
                                % You may adjust the margin values if needed, but the left and right
                                % margins must remain symmetrical to comply with Imperial regulation 4.3.

% ------------------------------------------------------
% Bibliography (BibLaTeX + Biber)
% ------------------------------------------------------
\usepackage[
    backend=biber,              % Biber is the recommended backend for BibLaTeX.
                                % It supports modern features such as UTF-8, DOIs,
                                % URLs, and complex name formats.
                                % More reliable and flexible than BibTeX.

    style=authoryear,           % Citation style used throughout the thesis.
                                % Produces citations like "Smith (2020)" or "(Smith, 2020)".
                                % Imperial does not prescribe a specific style,
                                % but author–year formats are standard in engineering,
                                % design research, and most scientific disciplines.

    maxcitenames=2              % Limits in-text citations to two authors before "et al.".
                                % Example: "Smith & Doe (2021)" or "Smith et al. (2021)".
]{biblatex}

\addbibresource{bibliography.bib} 
                                % Loads the .bib file containing all references.
                                % Students maintain this file manually or export it
                                % from Mendeley, Zotero, EndNote, etc.
                                %
                                % BibLaTeX is fully acceptable under Imperial guidelines:
                                % - The checklist does not mandate any specific reference style.
                                % - It only requires a consistent format throughout the thesis.

% ------------------------------------------------------
% Section headings
% ------------------------------------------------------
\usepackage{sectsty}
\allsectionsfont{\normalfont\scshape}
                                % Converts section headings to small caps.
                                % Allowed under Section 4.6 (formatting not explicitly regulated).
                                % Good practice for clean academic typography.

% ------------------------------------------------------
% Custom commands
% ------------------------------------------------------
\newcommand{\degree}{Ph\ensuremath{.\!}D.\xspace}
                                % Convenience macro for correctly typesetting “Ph.D.”


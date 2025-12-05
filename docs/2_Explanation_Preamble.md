## Preamble Explanation

The **preamble** in a LaTeX document is a section defined *before* `\begin{document}`that controls the **formatting, structure, typography, citation style, margins, and overall layout** of the entire thesis.

In this template, the preamble is configured to ensure:

✅ Compliance with **Imperial College Thesis Requirements** (Sections 4.1–4.6)  
✅ Correct margins and page layout as required by **Regulation 4.3**  
✅ Continuous Arabic numbering from the title page as required by **Regulation 4.4**  
✅ Professional typesetting of text, figures, tables, and mathematics  
✅ Clear, accessible PDF structure for electronic submission  
✅ A clean and modern academic style appropriate for different scientific fields.

Students normally do not need to modify the preamble, but understanding it helps ensure your thesis remains compliant and professionally formatted.

---

<!-- SNIPPET: preamble -->
```latex
% ------------------------------------------------------
% Encoding and Fonts
% ------------------------------------------------------
\usepackage[utf8]{inputenc}         % Allows UTF-8 characters (e.g., é, ñ, ü).
                                    % Recommended: ensures your thesis handles
                                    % international characters correctly.

\usepackage[T1]{fontenc}            % Improves hyphenation and PDF text extraction.
                                    % Good practice for long academic documents.

\usepackage{lmodern}                % Modern, scalable Latin font family.
                                    % Clean and readable for printed theses.

\usepackage{microtype}              % Improves spacing between letters/words.
                                    % Optional but highly recommended for quality typography.

% ------------------------------------------------------
% Mathematics
% ------------------------------------------------------
\usepackage{amsmath,amssymb}        % Essential math packages for equations, symbols,
                                    % matrices, aligned environments, etc.

% ------------------------------------------------------
% Figures and Captions
% ------------------------------------------------------
\usepackage{graphicx}               % Required to insert images using \includegraphics.
                                    % To scale images: use width=0.5\textwidth, height=..., etc.

\usepackage{caption}                % Controls caption style/spacing.
                                    % To modify caption size: \captionsetup{font=small}

\usepackage{subcaption}             % Allows subfigures (a), (b), etc.
                                    % Useful for 2×2 or side-by-side image layouts.

% ------------------------------------------------------
% Links and PDF Navigation
% ------------------------------------------------------
\usepackage{hyperref}               % Adds clickable links in the PDF.
                                    % Automatically links citations, TOC entries, figures.

\usepackage{bookmark}               % Improves PDF bookmarks stability.
                                    % Best practice for long theses.

% ------------------------------------------------------
% Tables
% ------------------------------------------------------
\usepackage{booktabs}               % High-quality table rules: \toprule, \midrule, \bottomrule.
                                    % For professional-looking tables.

% ------------------------------------------------------
% Acronyms and Nomenclature
% ------------------------------------------------------
\usepackage{acronym}                % For lists of acronyms (optional).

\usepackage{nomencl}                % Creates a nomenclature (list of symbols).
\makenomenclature                   % Generates the nomenclature file.
                                    % Run "makeindex thesis.nlo -s nomencl.ist -o thesis.nls"
                                    % or use Overleaf's built-in tool.

% ------------------------------------------------------
% Page Layout (Margins)
% ------------------------------------------------------
\usepackage{geometry}               
\geometry{
  a4paper,
  inner=3cm, outer=3cm,             % Left/right margins — MUST be symmetrical 
                                    % to satisfy Imperial Thesis Regulation 4.3.
  top=3cm, bottom=3cm
}
                                    % To change margins: modify these values.
                                    % Keep left = right to maintain centred page content.

% ------------------------------------------------------
% Code Listings
% ------------------------------------------------------
\usepackage{minted}                 % For syntax-highlighted code blocks (Python, C++, etc.).
                                    % Usage: \begin{minted}{python} ... \end{minted}
                                    %
                                    % IMPORTANT:
                                    % Overleaf → Menu → Compiler → Enable “Shell escape”.
                                    % Without shell-escape, minted will not compile.

% ------------------------------------------------------
% Bibliography (BibLaTeX + Biber)
% ------------------------------------------------------
\usepackage[
  backend=biber,                    % Biber handles UTF-8, DOIs, URLs, many authors, etc.
  style=authoryear,                 % Produces citations like Smith (2020).
  maxcitenames=2                    % Use “et al.” after 2 authors.
]{biblatex}

\addbibresource{bibliography.bib}   % Main bibliography file.
                                    % Export references from Mendeley, Zotero, etc.
                                    %
                                    % Imperial does NOT mandate a specific citation style.
                                    % Any consistent academic style is acceptable.

% ------------------------------------------------------
% Section Heading Style
% ------------------------------------------------------
\usepackage{sectsty}
\allsectionsfont{\normalfont\scshape}
                                    % Converts section titles to small caps.
                                    % Optional: change to \bfseries or remove styling entirely.

% ------------------------------------------------------
% Custom Commands
% ------------------------------------------------------
\newcommand{\degree}{Ph\ensuremath{.\!}D.\xspace}
                                    % Convenience macro for correctly typesetting "Ph.D."
                                    % You can define similar commands for common terms.
```
```latex
(placeholder – will be replaced)

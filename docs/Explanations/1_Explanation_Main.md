## 🎓 Introduction

The *Imperial College London Thesis Submission Checklist* outlines the essential requirements for PhD thesis formatting and structure, but it does **not provide strict or exhaustive layout specifications**.  
This leaves flexibility for candidates to decide how to design and typeset their thesis, as long as the document contains all required elements in the correct order. 

This document serves four main purposes:

1. **Explain** the official requirements defined in the Thesis Submission Checklist and related Imperial College regulations.  
2. **Demonstrate** how each requirement has been implemented in this LaTeX template — linking each rule to the corresponding code snippet or environment.  
3. **Recommend best practices** in academic typesetting, presentation, and structure to help produce a professional-quality thesis.  
4. **Empower users** to understand the reasoning behind each implementation so they can confidently make their own adjustments while remaining compliant with Imperial College’s regulations.

By combining regulatory guidance with technical explanations, this document helps PhD students not only use the provided template effectively but also **customize it responsibly**, ensuring their thesis remains compliant, well-formatted, and professionally presented.

## ⚙️ Document Settings

Every LaTeX document begins by declaring its **class**; this determines the overall structure, formatting, and layout rules used by the compiler.  
For this thesis template, the following declaration is used:

```latex
\documentclass[11pt, twoside, openany]{book} 
% 'book' provides chapters, front matter, appendices and a well-structured layout suitable for theses.
% 
% '11pt' sets the base font size. You may select 10pt or 12pt if desired, but 11pt offers excellent readability.
%
% 'twoside' produces a double-sided layout (odd/even pages).
% IMPORTANT: Imperial Thesis Regulation 4.3 requires *centred* text with symmetrical margins—handled in the preamble.
%
% 'openany' allows chapters to begin on either left or right pages.
% For a more traditional thesis layout, use 'openright' (chapters always begin on odd-numbered pages).
%
% Full details about margins, fonts, and styling are explained in the PREAMBLE.
```

### 🏛️ Preamble and Title Page

Because of their length and complexity, the preamble and title page have been given dedicated pages for detailed explanation. The code snippet below loads the preamble, configures headers/footers and page numbering, and inserts the title page:

```latex
\input{preamble.tex}  % Loads all global formatting, packages, and margin settings.

% -------------------------------
% Header and Footer Style
% -------------------------------
\usepackage{fancyhdr}  
% The 'fancyhdr' package gives full control over headers and footers.
% Students can customise:
%   - page numbers (left/centre/right)
%   - add chapter titles in the header
%   - add rules/lines or remove them
%   - different layouts for odd/even pages when using 'twoside'

\pagestyle{fancy}   % Apply the fancy header/footer style.
\fancyhf{}          % Clear all header and footer fields.
\fancyfoot[C]{\thepage}   % Page number centred at the bottom (Regulation 4.4).

\renewcommand{\headrulewidth}{0pt}  % Remove top horizontal line.
\renewcommand{\footrulewidth}{0pt}  % Remove bottom horizontal line.

% -------------------------------
% START OF DOCUMENT
% -------------------------------
\begin{document}

% -------------------------------
% Title Page
% -------------------------------
\pagenumbering{arabic}  % Imperial requires Arabic page numbers starting on the title page.
\setcounter{page}{1}    % Title page = Page 1
\input{titlepage.tex}   % Loads your custom title page.
```

### 📄 Dedication

The *Imperial College London Thesis Submission Checklist* does **not require** a Dedication page. Including one is **entirely optional**. By convention, Dedications usually appear near the beginning of a thesis, but their exact placement is flexible.

Below is the LaTeX structure used for the dedication page in this template:

```latex
% -------------------------------
% Dedication Page
% -------------------------------
\thispagestyle{plain}   % Plain page style = page number only, centred at bottom.
\vspace*{5cm}           % Move dedication text downwards. Modify value to adjust placement.

\begin{center}
    \emph{To my family,\\  
    and friends.}
    % Replace with your personal dedication text.
    % Using \emph makes the text italicised.
\end{center}
```

### 📜 Declaration of Originality

Imperial requires a **Statement of Originality** near the beginning of the thesis. The following snippet implements this requirement and includes a copyright statement:

```latex
% -------------------------------
% Declaration of Originality
% -------------------------------
\clearpage
\thispagestyle{plain}
\vspace*{4cm}

\noindent 
I hereby declare that this thesis and the work presented herein is my own work except where appropriately referenced or acknowledged.
% Mandatory statement confirming originality of the thesis.

\vspace{0.5cm}

\noindent
\textbf{Your Name}   % Replace with your full name.
                      % Good practice: sign physically after printing.

\vspace{5cm}

\noindent
% Required copyright statement (Imperial thesis checklist, Section 6)
The copyright of this thesis rests with the author and is made available under a Creative Commons Attribution-Non Commercial-No Derivatives license…
```

### 📑 Abstract — Compliance with §7.1

According to the checklist, the **title page must be followed by an abstract of no more than 300 words**. The template defines the abstract section as follows:

```latex
% -------------------------------
% Abstract (MANDATORY)
% -------------------------------
\clearpage
\chapter*{Abstract}
% Imperial requires an abstract of no more than 300 words.
% The abstract provides a concise summary of the thesis.
```

### 🙏 Acknowledgements

Acknowledgements are **optional** but common. They allow you to thank supervisors, collaborators, family, friends, and funders. Imperial does not mandate their exact location.

The LaTeX structure used in this template is:

```latex
% -------------------------------
% Acknowledgements (Optional)
% -------------------------------
\clearpage
\chapter*{Acknowledgements}
% Not mandatory, but standard in most theses.
% Thank supervisors, collaborators, family, funding agencies.
```

### 📣 Dissemination

This optional section lists publications, posters and other research outputs related to the thesis:

```latex
% -------------------------------
% Dissemination (Optional)
% -------------------------------
\clearpage
\chapter*{Dissemination}
% Optional section listing publications, posters, conference papers, preprints, etc.
\begin{itemize}
    \item Paper 1: Title, Journal/Conference, Year
    \item Paper 2: Title, Journal/Conference, Year
    \item Poster 1: Title, Conference, Year
\end{itemize}
% START END: Dissemination

% START SNIPPET: Nomenclature_Acronyms
% -------------------------------
% Nomenclature (Optional)
% -------------------------------
\clearpage
\printnomenclature
% If the page appears empty: ensure you ran `makeindex` for the nomenclature file.

% -------------------------------
% Acronyms (Optional)
% -------------------------------
\clearpage
\chapter*{Acronyms}
\input{phd-thesis/Acronym}
% Add or modify acronyms in the Acronym.tex file.
% END SNIPPET: Nomenclature_Acronyms

% START SNIPPET: Contents, List of Figures/Tables
% -------------------------------
% Contents, List of Figures/Tables
% -------------------------------
\clearpage
\tableofcontents
\listoffigures
\listoftables
% LaTeX generates these automatically.
% If items do not appear, compile *twice*.
% END SNIPPET: Contents, List of Figures/Tables

% START SNIPPET: CHAPTERS
% -------------------------------
% MAIN CHAPTERS
% -------------------------------
\chapter{Introduction}
\input{chapters/01-introduction.tex}

\chapter{Related Work}
\input{chapters/02-related-work.tex}

\chapter{Methods}
\input{chapters/03-methods.tex}

\chapter{Results}
\input{chapters/04-results.tex}

\chapter{Discussion}
\input{chapters/05-discussion.tex}

\chapter{Conclusion}
\input{chapters/06-conclusion.tex}
% END SNIPPET: CHAPTERS

% START SNIPPET: APPENDIX
% -------------------------------
% APPENDIX
% -------------------------------
\appendix
\chapter{Appendix A}
% Add additional appendices as needed: \chapter{Appendix B}, etc.

% -------------------------------
% Code Example (minted)
% -------------------------------
% Example of including syntax-highlighted code.
% Make sure shell-escape is enabled in your LaTeX compiler.
% Overleaf → Menu → Settings → Compiler → Enable "Shell escape".
\begin{minted}{python}
import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

side1 = 3
side2 = 4
hypotenuse = pythagoras(side1, side2)
print("Hypotenuse:", hypotenuse)
\end{minted}
% END SNIPPET: APPENDIX

% START SNIPPET: Bibliography
% -------------------------------
% Bibliography
% -------------------------------
\backmatter
\printbibliography   % Automatically formats the bibliography using BibLaTeX.
% END SNIPPET: Bibliography

\end{document}
```

### 📚 Nomenclature & Acronyms

This template provides optional sections for **nomenclature** and **acronyms**:

```latex
% -------------------------------
% Nomenclature (Optional)
% -------------------------------
\clearpage
\printnomenclature
% If the page appears empty: ensure you ran `makeindex` for the nomenclature file.

% -------------------------------
% Acronyms (Optional)
% -------------------------------
\clearpage
\chapter*{Acronyms}
\input{phd-thesis/Acronym}
% Add or modify acronyms in the Acronym.tex file.
```

### 📋 Contents and Lists

Imperial requires a **table of contents** and lists of figures/tables after the abstract and front matter. This template uses:

```latex
% -------------------------------
% Contents, List of Figures/Tables
% -------------------------------
\clearpage
\tableofcontents
\listoffigures
\listoftables
% LaTeX generates these automatically.
% If items do not appear, compile *twice*.
```

### 📘 Main Chapters

The main body of the thesis is organised into numbered chapters:

```latex
% -------------------------------
% MAIN CHAPTERS
% -------------------------------
\chapter{Introduction}
\input{chapters/01-introduction.tex}

\chapter{Related Work}
\input{chapters/02-related-work.tex}

\chapter{Methods}
\input{chapters/03-methods.tex}

\chapter{Results}
\input{chapters/04-results.tex}

\chapter{Discussion}
\input{chapters/05-discussion.tex}

\chapter{Conclusion}
\input{chapters/06-conclusion.tex}
```

### 📎 Appendices

Appendices follow the bibliography and may include additional material and permissions:

```latex
% -------------------------------
% APPENDIX
% -------------------------------
\appendix
\chapter{Appendix A}
% Add additional appendices as needed: \chapter{Appendix B}, etc.

% -------------------------------
% Code Example (minted)
% -------------------------------
% Example of including syntax-highlighted code.
% Make sure shell-escape is enabled in your LaTeX compiler.
% Overleaf → Menu → Settings → Compiler → Enable "Shell escape".
\begin{minted}{python}
import math

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

side1 = 3
side2 = 4
hypotenuse = pythagoras(side1, side2)
print("Hypotenuse:", hypotenuse)
\end{minted}
```

### 📖 Bibliography

The bibliography is generated automatically from your `.bib` file:

```latex
% -------------------------------
% Bibliography
% -------------------------------
\backmatter
\printbibliography   % Automatically formats the bibliography using BibLaTeX.
```



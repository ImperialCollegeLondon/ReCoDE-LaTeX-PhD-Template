## 🎓 Introduction

The *Imperial College London Thesis Submission Checklist* defines the essential requirements for the structure, contents, and presentation of a thesis, but it does **not prescribe a single fixed layout**.  
This gives candidates flexibility in how they design and typeset their work, provided that:

- All required elements are included.
- The order of elements follows the regulations.
- The document is clear, legible, and professionally presented.

This document serves four main purposes:

1. **Explain** the official requirements defined in the Thesis Submission Checklist and related Imperial College regulations.  
2. **Show** how each requirement has been implemented in this LaTeX template, by linking rules to specific code snippets.  
3. **Recommend good practice** in academic typesetting and document design.  
4. **Help you adapt the template** confidently while remaining compliant with Imperial’s rules.

By combining regulatory guidance with technical explanations, this document is intended to help you both **use** and **customise** the template responsibly.

---

## ⚙️ Document Settings — `\documentclass`

Every LaTeX document starts by declaring its **document class**, which determines the overall structure and many formatting defaults (chapters, sections, margins, floats, etc.).

In this template we use the following declaration:

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

This choice supports Imperial’s expectations in several ways:

- The `book` class provides **chapters**, **front matter**, and **appendices**, matching the typical structure of a PhD thesis.
- A base font size of **11pt** gives good readability for a long document.
- The `twoside` option prepares a **double‑sided layout** (odd/even pages), which is standard for theses.
- The `openany` option allows chapters to begin on **any page**; if you prefer a more traditional layout where chapters always start on a right‑hand page, you can change this to `openright`.

Imperial’s Presentation guidance requires that **page content is centred**, with symmetrical margins. The technical implementation of that requirement lives mainly in the **preamble**, described next.

---

## 🏛️ Preamble, Headers/Footers, and Title Page

The **preamble** collects all global formatting: packages, margins, page style, and other settings.  
This template loads a separate `preamble.tex` and then configures:

- Headers and footers.
- Page numbering.
- The title page.

The corresponding code is:

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

How this relates to the checklist:

- The use of a custom page style with `\fancyfoot[C]{\thepage}` produces **page numbers centred at the bottom**, which is consistent with Imperial’s requirement that pages be numbered clearly and consistently.
- The commands that set `\pagenumbering{arabic}` and `\setcounter{page}{1}` ensure that:
  - The **title page is page 1**.
  - **Arabic numerals** are used from the first page and continue in a single sequence throughout the thesis.

The title page itself (defined in `titlepage.tex`) must include:

- The **approved title** of the thesis.
- Your **full name**, as registered at the College.
- “Imperial College London” and the **Department** name.
- The **degree** for which the thesis is submitted (e.g. PhD, MPhil, EngD, MD(Res)).

These items are explicitly required in the Presentation section of the checklist.

---

## 📄 Dedication (Optional)

The *Imperial College London Thesis Submission Checklist* does **not** require a dedication page. Including one is entirely optional, and its position is not rigidly specified.

By convention, a dedication:

- Appears early in the thesis.
- Contains a short, personal statement.

This template provides a simple dedication page:

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

You can:

- Replace the example text with your own dedication.
- Adjust the vertical spacing so the text appears higher or lower on the page.

---

## 📜 Declaration of Originality (Required)

The checklist requires that candidates include a **Statement of Originality** at the beginning of the thesis.  
In your own words, you must confirm that:

- The work is your own.
- All other work is properly referenced or acknowledged.

This template includes a dedicated Declaration of Originality page:

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

To use it correctly:

- Replace `Your Name` with your full registered name.
- If needed, adjust the wording while keeping the meaning: that the thesis is your own work and that all sources are appropriately acknowledged.

Immediately following (or combined with) this statement, the template also includes a **copyright declaration**, required because the final thesis will be deposited in **Spiral** and made available for public reference.

---

## ©️ Copyright Declaration and Licence (Required)

Imperial requires a **copyright statement** near the beginning of the thesis.  
The final, corrected thesis will be stored electronically in **Spiral**, the College’s repository, and normally made **open access** after any embargo period.

The checklist notes:

- You are allowed to choose from **any Creative Commons licence** for your thesis.
- If you do not need a specific alternative, the College recommends a **Creative Commons Attribution–Non Commercial 4.0 International (CC BY‑NC 4.0)** licence.

In this template, the copyright statement in the **Declaration of Originality** snippet should be edited so that it:

- Names the licence you choose (e.g. “Creative Commons Attribution‑Non Commercial 4.0 International Licence (CC BY‑NC)”).
- Makes clear that re‑users must credit the author and cannot use the work for commercial purposes.

You should also ensure that any text you include aligns with the more detailed guidance provided by the College on copyright and Creative Commons licences.

---

## 📑 Abstract — Compliance with §7.1

According to the checklist (section 7.1):

> “The title-page should be followed by an abstract consisting of no more than **300 words**.”

This template enforces the correct position and provides the structure for the abstract:

```latex
% -------------------------------
% Abstract (MANDATORY)
% -------------------------------
\clearpage
\chapter*{Abstract}
% Imperial requires an abstract of no more than 300 words.
% The abstract provides a concise summary of the thesis.
```

Key points:

- The abstract appears on its own page immediately after the front‑matter pages (title, declarations).
- It must be **no longer than 300 words**.
- It should briefly summarise:
  - The research problem or question.
  - The methods used.
  - The main results.
  - The significance of the findings.

LaTeX does **not** count words for you, so you should check the word count manually.

---

## 🙏 Acknowledgements (Optional but Common)

The checklist does **not** prescribe an Acknowledgements section, but it is standard practice in PhD theses.  
It is typically used to:

- Thank supervisors and co‑supervisors.
- Acknowledge collaborators, technical and administrative staff.
- Mention family, friends, and funding bodies.

This template includes an unnumbered Acknowledgements chapter:

```latex
% -------------------------------
% Acknowledgements (Optional)
% -------------------------------
\clearpage
\chapter*{Acknowledgements}
% Not mandatory, but standard in most theses.
% Thank supervisors, collaborators, family, funding agencies.
```

Imperial does not specify a fixed position for this section. Common conventions include:

- Placing it after the abstract and before the table of contents, or
- Placing it after the conclusion.

You may move this block in the LaTeX source if your department has a preferred location.

---

## 📣 Dissemination (Optional)

The checklist does not explicitly mention a **Dissemination** section, but it can be helpful to document research outputs associated with the thesis, such as:

- Published journal articles.
- Conference papers and posters.
- Preprints and technical reports.

This template includes an optional Dissemination chapter:

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
```

You can edit the list to include your actual publications and outputs.  
This section is intended for information only and is not formally examined as a separate requirement.

---

## 📚 Nomenclature and Acronyms (Optional)

While the checklist does not explicitly require **nomenclature** or **lists of acronyms**, including them can make technical theses significantly easier to read.

This template provides:

- An optional **Nomenclature** section for symbols and notation.
- An **Acronyms** section for abbreviations used in the thesis.

The corresponding code is:

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

To use these sections:

- Define your nomenclature entries and ensure you run the necessary indexing commands so that `\printnomenclature` outputs a list.
- Edit the acronyms file to add each abbreviation and its full form.

---

## 📋 Contents, List of Figures, and List of Tables

The checklist requires the abstract to be followed by a **full table of contents**, and also expects lists of tables, figures, photographs, and any other additional materials.

This template generates these automatically:

```latex
% -------------------------------
% Contents, List of Figures/Tables
% -------------------------------
\clearpage
\tableofcontents
% This command tells LaTeX to generate the Table of Contents automatically.
% LaTeX collects all headings (chapters, sections, subsections, etc.) as it compiles and writes them to a helper file with extension .toc. On the next % compilation, it reads that .toc file and uses it to typeset the full table of contents with titles and page numbers.
% If a new section or chapter doesn’t show up in the contents, you usually just need to compile the document at least twice.

\listoffigures
% This command generates a “List of Figures”.
% Every time you use the figure environment together with a \caption{...}, LaTeX records that figure in a helper file with extension .lof. On the next % compilation, it reads that .lof file and prints a list showing each figure number, its caption, and the page number.
% If the list is missing new figures or the page numbers look wrong, compile again so the .lof file is updated and then used.

\listoftables
% This command generates a “List of Tables”.
% Every time you use the table environment with a \caption{...}, LaTeX records that table in a helper file with extension .lot. 
% On the next compilation, it reads that .lot file and prints a list showing each table number, its caption, and the page number.
% As with the other lists, after adding or renumbering tables you usually need at least two compilations for the list to become correct and up to date.

```

How this relates to the regulations:

- The **Table of Contents** must list the major structural elements of the thesis, including chapters and any separately supplied material.
- The **List of Figures** and **List of Tables** provide quick reference for visual material and tables used throughout the thesis.

In LaTeX:

- `\tableofcontents` collects all headings from the compiled document.
- `\listoffigures` lists every figure that has a caption.
- `\listoftables` lists every table that has a caption.

If new chapters, figures, or tables do not appear, simply compile the document again so that LaTeX can update its auxiliary files.

---

## 📘 Main Chapters

The main body of the thesis is organised into **numbered chapters**.  
The checklist does not mandate exact chapter titles or structure, but typical PhD theses include:

- An **Introduction** (context, aims, overview).
- A **Related Work** or **Literature Review** chapter.
- **Methods** or **Materials and Methods**.
- **Results**.
- **Discussion**.
- **Conclusion**.

This template sets up a representative structure:

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

Each chapter is stored in its own `.tex` file under `chapters/`, which keeps the main file readable and makes it easier to reorganise or expand content.

---

## 📎 Appendices

The checklist states that appendices should appear **after the bibliography** and should include:

- Data and material that examiners might wish to refer to but are not expected to examine in detail.
- Copies of all **permission documents** showing that you have permission to reproduce any third‑party copyrighted works in your thesis.

This template defines the appendix section like this:

```latex
% -------------------------------
% APPENDIX
% -------------------------------
\appendix
\chapter{Appendix A}
% Add additional appendices as needed: \chapter{Appendix B}, etc.
```

You can add additional appendices (`Appendix B`, `Appendix C`, etc.) for:

- Supplementary derivations or proofs.
- Extended tables or additional figures.
- Copies of permission letters and copyright licences.

---

## 📖 Bibliography

A complete **bibliography** of all works cited in the thesis is required.  
The checklist does not enforce a specific referencing style, but your department may recommend or require one (e.g. numeric, Harvard, Vancouver, APA).

This template uses BibLaTeX to generate the bibliography:

```latex
% -------------------------------
% Bibliography
% -------------------------------
\backmatter
\printbibliography   % Automatically formats the bibliography using BibLaTeX.
```

To use it correctly:

- Maintain your references in one or more `.bib` files.
- Configure the citation and bibliography style in `preamble.tex` according to your discipline’s expectations.
- Run the appropriate compile cycle (LaTeX ➝ Biber/BibTeX ➝ LaTeX) so that citations and bibliography entries are fully resolved.

The bibliography should appear **before** the appendices to match the normal academic convention and the structure implied by the checklist.

---

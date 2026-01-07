## 🎓 Introduction

The [Theses for Imperial College Research Degrees](https://www.imperial.ac.uk/media/imperial-college/administration-and-support-services/registry/academic-governance/public/academic-policy/research-degree-examinations/Thesis-Submission-Checklist.pdf) document describes the submission, format and requirements for theses submitted for the degrees of MPhil, PhD, MD(Res) and EngD.

It specifies:

- **Administrative rules** (submission route, declaration form, embargoes) – Sections 1–3, 12  
- **Presentation rules** (layout, spacing, numbering, title page) – Section 4  
- **Front‑matter requirements** (statement of originality, copyright, abstract, table of contents) – Sections 5–8  
- **Back‑matter requirements** (appendices, illustrative material) – Sections 9–10  
- **Legal and ethical checks** (copyright, plagiarism, IP) – Section 11  

The LaTeX files of the template are found in the [phd-thesis](https://github.com/ImperialCollegeLondon/ReCoDE-LaTeX-PhD-Template/tree/main/phd-thesis) directory. This explanation document shows how the provided LaTeX template:

- Implements the college theses requirements in `phd-thesis/main.tex`.
- Links each rule to a **snippet** (marked by `% START/END SNIPPET` in the LaTeX and `<!-- SNIPPET:... -->` here).
- Leaves reasonable freedom where the checklist explicitly allows it (Section 4.6).
---

## Snippets

When examining the LaTeX files of this template, you will notice that certain important sections are marked as **snippets** using comments such as `% START/END SNIPPET`. You can ignore these comments when reading the LaTeX code; they are only there to help with the generation of these documentation pages. You can/should remove them to declutter your document.

---

## ⚙️ Document Settings — `\documentclass`  
*(Checklist Section 4 – Presentation: legibility and overall structure)*

Every LaTeX document begins by declaring its **document class**, which governs the overall structure and many default formatting choices.

In this template we use:

```latex
\documentclass[11pt, twoside, openany]{book} 
% 'book' provides chapters, front matter, appendices and a well-structured layout suitable for theses.
% 
% '11pt' sets the base font size. You may select 10pt or 12pt if desired, but 11pt offers excellent readability.
%
% 'twoside' produces a double-sided layout (odd/even pages).
% IMPORTANT: Checklist Section 4.3 requires *centred* text with symmetrical margins—handled in the preamble.
%
% 'openany' allows chapters to begin on either left or right pages.
% For a more traditional thesis layout, use 'openright' (chapters always begin on odd-numbered pages).
%
% Full details about margins, fonts, and styling are explained in the PREAMBLE.
```

This supports the **Presentation** requirements in Section 4 as follows:

- `book` provides **chapters, front matter and appendices**, matching a thesis‑style structure.
- A base font size of 11pt helps ensure the thesis is **“easily legible for examiners and illustrates information, diagrams, tables etc. clearly”** (Section 4.1).
- `twoside` anticipates double‑sided printing, which is natural for a long document.
- `openany` allows chapters to begin on either left‑ or right‑hand pages; you may change to `openright` if you prefer the more traditional “chapters on right‑hand pages”.

The more specific rules in Section 4 (centred text, margins, spacing, numbering) are implemented in the **preamble** and **title page** configuration, described next.

---

## 🏛️ Preamble, Headers/Footers, Page Layout, and Title Page  
*(Checklist Section 4 – Presentation: Sections 4.1–4.6)*

Section **4 – Presentation** states that:

- **Section 4.1**: Electronic copies should be **easily legible** and clearly show information, diagrams, tables etc.  
- **Section 4.2**: You must correct errors; examiners are not proof‑readers.  
- **Section 4.3**: *“Page content should be centred, so that margins are equal distant from the edge of page. Double or one‑and‑a‑half spacing should be used, except for indented quotations or footnotes where single spacing may be used.”*  
- **Section 4.4**: *“All pages must be numbered in one continuous sequence, i.e. from the title page to the last page of type, in Arabic numerals from 1 onwards… including maps, diagrams, blank pages, etc.”*  
- **Section 4.5**: The **title page must bear**:

    - The approved thesis **title**.  
    - The candidate's **full name** (as registered).  
    - **Imperial College London** and the **Department** name.  
    - The **degree** (e.g. PhD)

- **Section 4.6**: Any formatting not explicitly outlined is left to the **student’s judgement**, and *reasonable solutions will be accepted*.

This template implements those rules via the preamble and title page block:

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
\fancyfoot[C]{\thepage}   % Page number centred at the bottom (Section 4.4).

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

How this snippet maps to Section 4:

- **Centred text and margins (Section 4.3)**  
  The actual margin and layout configuration is stored in `preamble.tex` (geometry, line spacing, etc.). It is designed so that the **text block is centred** on the page with **symmetrical margins**, directly satisfying Section 4.3.

- **Line spacing (Section 4.3)**  
  `preamble.tex` uses appropriate line‑spacing commands so that the **main text** is in double or one‑and‑a‑half spacing, while **footnotes and indented quotations** may use single spacing, as allowed by Section 4.3.

- **Continuous Arabic page numbering (Section 4.4)**  
  The snippet in `main.tex`:
  
      - switches to **Arabic numerals**;  
      - sets the **title page as page 1**;
  
  ensuring that all pages – from the title page through to the final page – form **one continuous Arabic sequence**, including pages with only diagrams or even intentionally blank ones, as required by Section 4.4.

- **Title page content (Section 4.5)**  
  The title page is defined in `titlepage.tex`, which is loaded here. It is constructed so that the title page contains exactly the items listed in Section 4.5:
  
      - the **approved title** of the thesis (matching examination entry);  
      - your **full name**, as registered at Imperial;  
      - **Imperial College London** and the **Department** name;  
      - the **degree** for which the thesis is submitted.

- **Reasonable formatting choices (Section 4.6)**  
  Fonts, chapter styles, and other typographic details are chosen to be professional and readable. Under Section 4.6, you may modify these choices (e.g. fonts, header style) as long as your changes remain **reasonable** and do not violate any explicit rules in Section 4.

Because `preamble.tex` and `titlepage.tex` are central to Section 4, this template also provides **separate explanation pages**:

- A **Preamble Explanation** describing layout, fonts, packages, and spacing.  
- A **Title‑Page Explanation** showing how each field satisfies Section 4.5.

---

## 📄 Dedication  
*(Not mentioned in checklist – optional)*

The checklist does **not** mention a dedication page; there is no numbered requirement for it in Sections 1–12.  
Including a dedication is therefore entirely **optional** and up to you.

By convention, a dedication:

- Appears near the beginning of the thesis.  
- Contains a short personal message.

This template includes an optional dedication page:

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

You may rewrite the text and adjust spacing as you like. No checklist requirement depends on this section.

---

## 📜 Declaration of Originality  
*(Checklist Section 5 – Statement of Originality: Sections 5.1–5.2)*

Section **5 – Statement of Originality** states:

- **Section 5.1**: *“Candidates must include a short statement in your own words, that the work is your own and that all else is appropriately referenced.”*  
- **Section 5.2**: *“The Statement of Originality should appear at the beginning of the thesis.”*

This template provides a Declaration of Originality page that implements Sections 5.1–5.2:

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

Compliance with Section 5:

- The text explicitly asserts that the **thesis and the work it presents are your own**, except where properly referenced or acknowledged, matching the wording of Section 5.1.
- You must replace `Your Name` with your **full registered name** to clearly identify yourself as the candidate.
- The declaration is positioned near the **beginning of the thesis**, as Section 5.2 requires.

You may adjust the phrasing, but it must keep the same meaning as Section 5.1 to remain compliant.

---

## ©️ Copyright Declaration and Licence  
*(Checklist Section 6 – Copyright Declaration: Sections 6.1–6.4)*

Section **6 – Copyright Declaration** states:

- **Section 6.1**: Because your thesis will be made available for **public reference**, the College requires a **copyright statement** at the beginning of your thesis.  
- **Section 6.2**: You may choose any of the **Creative Commons licences** when publishing your thesis on Spiral.  
- **Section 6.3**: If no specific licence is required, you are advised to use the CC BY‑NC 4.0 wording given in Section 6.3.  
- **Section 6.4**: You are advised to complete an online course on copyright.

In this template:

- The **copyright** text, placed together with the Declaration of Originality,  
  - states that copyright rests with the **author**;  
  - references a **Creative Commons licence**, consistent with Section 6.2;  
  - can be edited to match the recommended CC BY‑NC 4.0 wording in Section 6.3 if you wish.

To fully satisfy **Section 6.1–6.3**:

- Make sure the final text explicitly:

  - names the licence (e.g. *Creative Commons Attribution‑Non Commercial 4.0 International Licence (CC BY‑NC)*), and  
  - explains that reuse is allowed only under the licence conditions.

---

## 📑 Abstract  
*(Checklist Section 7 – Abstract: Section 7.1)*

Section **7 – Abstract** contains a single requirement:

- **Section 7.1**: *“The title-page should be followed by an abstract consisting of no more than 300 words.”*

This template enforces the correct structure:

```latex
% -------------------------------
% Abstract (MANDATORY)
% -------------------------------
\clearpage
\chapter*{Abstract}
% Imperial requires an abstract of no more than 300 words.
% The abstract provides a concise summary of the thesis.
```

To comply with **Section 7.1**:

- The abstract is placed **immediately after** the title page and declarations.  
- You must keep the abstract **within 300 words**.  
- It should concisely summarise:

  - the research problem or question;  
  - the methods used;  
  - the main results;  
  - the key conclusion or contribution.

LaTeX does not count words automatically; you must check the word count manually to ensure it complies with Section 7.1.

---

## 🙏 Acknowledgements  
*(Not numbered in checklist – standard practice)*

The checklist does **not** give a separate numbered section for **Acknowledgements** in Sections 1–12, and does not require them explicitly.  
However, acknowledgements are standard and expected in most theses.

Typical content:

- Thanks to supervisors and co‑supervisors.  
- Acknowledgement of collaborators, technical and administrative staff.  
- Recognition of funding bodies and personal support.

This template provides an Acknowledgements section:

```latex
% -------------------------------
% Acknowledgements (Optional)
% -------------------------------
\clearpage
\chapter*{Acknowledgements}
% Not mandatory, but standard in most theses.
% Thank supervisors, collaborators, family, funding agencies.
```

You may position this:

- After the abstract and before the table of contents, or  
- After the conclusion,  

as long as the required items (title page, abstract, contents, etc.) remain in the correct order defined by Sections 4–8.

---

## 📣 Dissemination  
*(Not mentioned in checklist – optional)*

The checklist does **not** mention a **Dissemination** section in Sections 1–12.  
It is therefore optional and provided as a convenience to list:

- Journal articles.  
- Conference papers and posters.  
- Preprints and related publications.

The template includes an optional Dissemination chapter:

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

You may freely edit or remove this section; it is not mandated by any checklist point.

---

## 📚 Nomenclature and Acronyms  
*(Not mentioned in checklist – optional)*

The checklist does not explicitly mention **nomenclature** or **acronym** lists.  
For technical and mathematical theses, these are good practice but not required.

This template offers optional sections:

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

Usage:

- Use **Nomenclature** for symbols and notation.  
- Use **Acronyms** to define abbreviations.  

These improve readability but are not tied to any specific paragraph in Sections 1–12.

---

## 📋 Table of Contents, List of Figures, and List of Tables  
*(Checklist Section 8 – Table of Contents: Section 8.1)*

Section **8 – Table of Contents** states:

- **Section 8.1**: *“The abstract should be followed by a full table of contents (including any additional material supplied separately to the main body of the thesis) and a list of tables, figures, photographs and any other materials.”*

This template implements **Section 8.1** with:

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

Mapping to Section 8.1:

- `\tableofcontents` gives the **full table of contents** immediately after the abstract, listing all chapters and sections and any additional material included in the document.  
- `\listoffigures` provides the **List of Figures**.  
- `\listoftables` provides the **List of Tables**.  

Together, they satisfy the requirement that the abstract be followed by a full ToC and lists of tables, figures, and other materials.

Note: LaTeX writes these lists to `.toc`, `.lof`, and `.lot` files during compilation; if something is missing, compile at least twice.

---

## 📘 Main Chapters  
*(Checklist: overall structure between Sections 4–9)*

The checklist defines the overall **order** of elements:

- Title page and required front matter (Sections 4–7)  
- Table of contents and lists (Section 8.1)  
- **Main body of the thesis**  
- Bibliography  
- Appendices (Section 9.1)

It does **not** prescribe specific chapter titles or internal structure for the main body; that is left to discipline‑specific conventions and Section 4.6 (“reasonable solutions”).

This template provides a typical structure:

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

Chapters are split into separate files under `chapters/`, which keeps `main.tex` readable and makes it easy to rearrange the main body while keeping the required overall order defined by the checklist.

---

## 📎 Appendices  
*(Checklist Section 9 – Appendices: Section 9.1)*

Section **9 – Appendices** states:

- **Section 9.1**: *“The appendices should be at the end of your thesis after your bibliography. It should include:  
  • Any data that the examiners may wish to refer to, but that they will not examine.  
  • Students must include copies of all permission documents showing that they have permission to republish all the third party copyrighted works in their thesis.”*

Think of appendices as a place for **evidence, examples, and supplementary detail**, not as an extension of the main argument. Good candidates for appendices include:

- Extended results, raw data samples, or additional figures.
- Long derivations, proofs, or technical specifications.
- Code listings and configuration files that illustrate how your methods were implemented.

Appendices should be **labelled and structured clearly** (e.g. Appendix A, B, C), and cross‑referenced from the main text where relevant. 

This template implements **Section 9.1** as follows:

```latex
% -------------------------------
% APPENDIX
% -------------------------------
\appendix
\chapter{Appendix A}
% Add additional appendices as needed: \chapter{Appendix B}, etc.
```

To comply with Section 9.1:

- Place all appendices **after the bibliography** in the final thesis.  
- Use them to store:

  - Supporting data that examiners may wish to consult but are not required to examine.  
  - Copies of all **permission documents** for third‑party material (figures, tables, images, maps, etc.).

You can create multiple appendix chapters (Appendix A, B, C, …) as needed.

---

## 📖 Bibliography  
*(Required; position implied by Section 8.1 and Section 9.1)*

The checklist expects a **full bibliography of works cited** in the thesis, although in your excerpt it is not given a separate numbered heading. Its position is implied by the structure:

- **Section 8.1** describes the abstract, table of contents, and lists.  
- **Section 9.1** explicitly states that appendices come **after your bibliography**.  

So the bibliography must appear **between** the main body and the appendices.

This template generates the bibliography with BibLaTeX:

```latex
% -------------------------------
% Bibliography
% -------------------------------
\backmatter
\printbibliography   % Automatically formats the bibliography using BibLaTeX.
```

This collects all cited works into a **complete bibliography** placed between the main chapters and the appendices, as required.

To use it:

- Maintain your references in `.bib` files.  
- Configure the reference style in `preamble.tex` to match your discipline and any departmental guidance.  
- Run LaTeX ➝ Biber/BibTeX ➝ LaTeX until all citations and bibliography entries are resolved.

This ensures that your thesis has a full, correctly positioned bibliography, consistent with the structure implied by **Section 8.1** and **Section 9.1** of the checklist.

---

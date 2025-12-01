## 🎓 Introduction

The *Theses for Imperial College Research Degrees: Guidance and notes* document describes the submission, format and requirements for theses submitted for the degrees of MPhil, PhD, MD(Res) and EngD.

It specifies:

- **Administrative rules** (submission route, declaration form, embargoes) – §§1–3, 12  
- **Presentation rules** (layout, spacing, numbering, title page) – §4  
- **Front‑matter requirements** (Statement of Originality, Copyright, Abstract, Table of Contents) – §§5–8  
- **Back‑matter requirements** (Appendices, illustrative material) – §§9–10  
- **Legal and ethical checks** (copyright, plagiarism, IP) – §11  

This explanation document shows how the provided LaTeX template:

1. Implements these requirements in `phd-thesis/main.tex`.
2. Links each rule to a **snippet** (marked by `% START/END SNIPPET` in the LaTeX and `<!-- SNIPPET:... -->` here).
3. Leaves reasonable freedom where the checklist explicitly allows it (§4.6).

All code snippets in this document are **automatically imported** from `main.tex`, so this explanation stays in sync with the actual template.

---

## ⚙️ Document Settings — `\documentclass`  
*(Checklist §4 – Presentation: legibility and overall structure)*

Every LaTeX document begins by declaring its **document class**, which governs the overall structure and many default formatting choices.

In this template we use:

<!-- SNIPPET: documentclass -->

This supports the **Presentation** requirements in §4 as follows:

- `book` provides **chapters, front matter and appendices**, matching a thesis‑style structure.
- A base font size of 11pt helps ensure the thesis is **“easily legible for examiners and illustrates information, diagrams, tables etc. clearly”** (§4.1).
- `twoside` anticipates double‑sided printing, which is natural for a long document.
- `openany` allows chapters to begin on either left‑ or right‑hand pages; you may change to `openright` if you prefer the more traditional “chapters on right‑hand pages”.

The more specific rules in §4 (centred text, margins, spacing, numbering) are implemented in the **preamble** and **title page** configuration, described next.

---

## 🏛️ Preamble, Headers/Footers, Page Layout, and Title Page  
*(Checklist §4 – Presentation: §§4.1–4.6)*

Section **4 – Presentation** states that:

- **§4.1**: Electronic copies should be **easily legible** and clearly show information, diagrams, tables etc.  
- **§4.2**: You must correct errors; examiners are not proof‑readers.  
- **§4.3**: *“Page content should be centred, so that margins are equal distant from the edge of page. Double or one‑and‑a‑half spacing should be used, except for indented quotations or footnotes where single spacing may be used.”*  
- **§4.4**: *“All pages must be numbered in one continuous sequence, i.e. from the title page to the last page of type, in Arabic numerals from 1 onwards… including maps, diagrams, blank pages, etc.”*  
- **§4.5**: The **title page must bear**:
  - The approved thesis **title**.  
  - The candidate’s **full name** (as registered).  
  - **Imperial College London** and the **Department** name.  
  - The **degree** (e.g. PhD).  
- **§4.6**: Any formatting not explicitly outlined is left to the **student’s judgement**, and *reasonable solutions will be accepted*.

This template implements those rules via the preamble and title page block:

<!-- SNIPPET: preamble_title -->

How this snippet maps to §4:

- **Centred text and margins (§4.3)**  
  The actual margin and layout configuration is stored in `preamble.tex` (geometry, line spacing, etc.). It is designed so that the **text block is centred** on the page with **symmetrical margins**, directly satisfying §4.3.

- **Line spacing (§4.3)**  
  `preamble.tex` uses appropriate line‑spacing commands so that the **main text** is in double or one‑and‑a‑half spacing, while **footnotes and indented quotations** may use single spacing, as allowed by §4.3.

- **Continuous Arabic page numbering (§4.4)**  
  The snippet in `main.tex`:
  - switches to **Arabic numerals**;  
  - sets the **title page as page 1**;  
  ensuring that all pages – from the title page through to the final page – form **one continuous Arabic sequence**, including pages with only diagrams or even intentionally blank ones, as required by §4.4.

- **Title page content (§4.5)**  
  The title page is defined in `titlepage.tex`, which is loaded here. It is constructed so that the title page contains exactly the items listed in §4.5:
  - the **approved title** of the thesis (matching examination entry);  
  - your **full name**, as registered at Imperial;  
  - **Imperial College London** and the **Department** name;  
  - the **degree** for which the thesis is submitted.

- **Reasonable formatting choices (§4.6)**  
  Fonts, chapter styles, and other typographic details are chosen to be professional and readable. Under §4.6, you may modify these choices (e.g. fonts, header style) as long as your changes remain **reasonable** and do not violate any explicit rules in §4.

Because `preamble.tex` and `titlepage.tex` are central to §4, this template also provides **separate explanation pages**:

- A **Preamble Explanation** describing layout, fonts, packages, and spacing.  
- A **Title‑Page Explanation** showing how each field satisfies §4.5.

---

## 📄 Dedication  
*(Not mentioned in checklist – optional)*

The checklist does **not** mention a dedication page; there is no numbered requirement for it in §§1–12.  
Including a dedication is therefore entirely **optional** and up to you.

By convention, a dedication:

- Appears near the beginning of the thesis.  
- Contains a short personal message.

This template includes an optional dedication page:

<!-- SNIPPET: dedication -->

You may rewrite the text and adjust spacing as you like. No checklist requirement depends on this section.

---

## 📜 Declaration of Originality  
*(Checklist §5 – Statement of Originality: §§5.1–5.2)*

Section **5 – Statement of Originality** states:

- **§5.1**: *“Candidates must include a short statement in your own words, that the work is your own and that all else is appropriately referenced.”*  
- **§5.2**: *“The Statement of Originality should appear at the beginning of the thesis.”*

This template provides a Declaration of Originality page that implements §§5.1–5.2:

<!-- SNIPPET: Declaration of Originality -->

Compliance with §5:

- The text explicitly asserts that the **thesis and the work it presents are your own**, except where properly referenced or acknowledged, matching the wording of §5.1.
- You must replace `Your Name` with your **full registered name** to clearly identify yourself as the candidate.
- The declaration is positioned near the **beginning of the thesis**, as §5.2 requires.

You may adjust the phrasing, but it must keep the same meaning as §5.1 to remain compliant.

---

## ©️ Copyright Declaration and Licence  
*(Checklist §6 – Copyright Declaration: §§6.1–6.4)*

Section **6 – Copyright Declaration** states:

- **§6.1**: Because your thesis will be made available for **public reference**, the College requires a **copyright statement** at the beginning of your thesis.  
- **§6.2**: You may choose any of the **Creative Commons licences** when publishing your thesis on Spiral.  
- **§6.3**: If no specific licence is required, you are advised to use the CC BY‑NC 4.0 wording given in §6.3.  
- **§6.4**: You are advised to complete an online course on copyright.

In this template:

- The **copyright** text, placed together with the Declaration of Originality,  
  - states that copyright rests with the **author**;  
  - references a **Creative Commons licence**, consistent with §6.2;  
  - can be edited to match the recommended CC BY‑NC 4.0 wording in §6.3 if you wish.

To fully satisfy **§6.1–6.3**:

- Make sure the final text explicitly:
  - names the licence (e.g. *Creative Commons Attribution‑Non Commercial 4.0 International Licence (CC BY‑NC)*), and  
  - explains that reuse is allowed only under the licence conditions.

---

## 📑 Abstract  
*(Checklist §7 – Abstract: §7.1)*

Section **7 – Abstract** contains a single requirement:

- **§7.1**: *“The title-page should be followed by an abstract consisting of no more than 300 words.”*

This template enforces the correct structure:

<!-- SNIPPET: Abstract -->

To comply with **§7.1**:

- The abstract is placed **immediately after** the title page and declarations.  
- You must keep the abstract **within 300 words**.  
- It should concisely summarise:
  - the research problem or question;  
  - the methods used;  
  - the main results;  
  - the key conclusion or contribution.

LaTeX does not count words automatically; you must check the word count manually to ensure it complies with §7.1.

---

## 🙏 Acknowledgements  
*(Not numbered in checklist – standard practice)*

The checklist does **not** give a separate numbered section for **Acknowledgements** in §§1–12, and does not require them explicitly.  
However, acknowledgements are standard and expected in most theses.

Typical content:

- Thanks to supervisors and co‑supervisors.  
- Acknowledgement of collaborators, technical and administrative staff.  
- Recognition of funding bodies and personal support.

This template provides an Acknowledgements section:

<!-- SNIPPET: Acknowledgements -->

You may position this:

- After the abstract and before the table of contents, or  
- After the conclusion,  

as long as the required items (title page, abstract, contents, etc.) remain in the correct order defined by §§4–8.

---

## 📣 Dissemination  
*(Not mentioned in checklist – optional)*

The checklist does **not** mention a **Dissemination** section in §§1–12.  
It is therefore optional and provided as a convenience to list:

- Journal articles.  
- Conference papers and posters.  
- Preprints and related publications.

The template includes an optional Dissemination chapter:

<!-- SNIPPET: Dissemination -->

You may freely edit or remove this section; it is not mandated by any checklist point.

---

## 📚 Nomenclature and Acronyms  
*(Not mentioned in checklist – optional)*

The checklist does not explicitly mention **nomenclature** or **acronym** lists.  
For technical and mathematical theses, these are good practice but not required.

This template offers optional sections:

<!-- SNIPPET: Nomenclature_Acronyms -->

Usage:

- Use **Nomenclature** for symbols and notation.  
- Use **Acronyms** to define abbreviations.  

These improve readability but are not tied to any specific paragraph in §§1–12.

---

## 📋 Table of Contents, List of Figures, and List of Tables  
*(Checklist §8 – Table of Contents: §8.1)*

Section **8 – Table of Contents** states:

- **§8.1**: *“The abstract should be followed by a full table of contents (including any additional material supplied separately to the main body of the thesis) and a list of tables, figures, photographs and any other materials.”*

This template implements **§8.1** with:

<!-- SNIPPET: Contents, List of Figures/Tables -->

Mapping to §8.1:

- `\tableofcontents` gives the **full table of contents** immediately after the abstract, listing all chapters and sections and any additional material included in the document.  
- `\listoffigures` provides the **List of Figures**.  
- `\listoftables` provides the **List of Tables**.  

Together, they satisfy the requirement that the abstract be followed by a full ToC and lists of tables, figures, and other materials.

Note: LaTeX writes these lists to `.toc`, `.lof`, and `.lot` files during compilation; if something is missing, compile at least twice.

---

## 📘 Main Chapters  
*(Checklist: overall structure between §§4–9)*

The checklist defines the overall **order** of elements:

- Title page and required front matter (§§4–7)  
- Table of contents and lists (§8.1)  
- **Main body of the thesis**  
- Bibliography  
- Appendices (§9.1)

It does **not** prescribe specific chapter titles or internal structure for the main body; that is left to discipline‑specific conventions and §4.6 (“reasonable solutions”).

This template provides a typical structure:

<!-- SNIPPET: CHAPTERS -->

Chapters are split into separate files under `chapters/`, which keeps `main.tex` readable and makes it easy to rearrange the main body while keeping the required overall order defined by the checklist.

---

## 📎 Appendices  
*(Checklist §9 – Appendices: §9.1)*

Section **9 – Appendices** states:

- **§9.1**: *“The appendices should be at the end of your thesis after your bibliography. It should include:  
  • Any data that the examiners may wish to refer to, but that they will not examine.  
  • Students must include copies of all permission documents showing that they have permission to republish all the third party copyrighted works in their thesis.”*

This template implements **§9.1** as follows:

<!-- SNIPPET: APPENDIX -->

To comply with §9.1:

- Place all appendices **after the bibliography** in the final thesis.  
- Use them to store:
  - Supporting data that examiners may wish to consult but are not required to examine.  
  - Copies of all **permission documents** for third‑party material (figures, tables, images, maps, etc.).

You can create multiple appendix chapters (Appendix A, B, C, …) as needed.

---

## 📖 Bibliography  
*(Required; position implied by §8.1 and §9.1)*

The checklist expects a **full bibliography of works cited** in the thesis, although in your excerpt it is not given a separate numbered heading. Its position is implied by the structure:

- **§8.1** describes the abstract, table of contents, and lists.  
- **§9.1** explicitly states that appendices come **after your bibliography**.  

So the bibliography must appear **between** the main body and the appendices.

This template generates the bibliography with BibLaTeX:

<!-- SNIPPET: Bibliography -->

How this fits §§8.1 and 9.1:

- It collects all cited works into a **complete bibliography**.  
- By placing this snippet **before** the Appendices snippet in `main.tex`, the bibliography naturally appears before the appendices, as §9.1 requires.

To use it:

- Maintain your references in `.bib` files.  
- Configure the reference style in `preamble.tex` to match your discipline and any departmental guidance.  
- Run LaTeX ➝ Biber/BibTeX ➝ LaTeX until all citations and bibliography entries are resolved.

This ensures that your thesis has a full, correctly positioned bibliography, consistent with the structure implied by **§8.1** and **§9.1** of the checklist.

---

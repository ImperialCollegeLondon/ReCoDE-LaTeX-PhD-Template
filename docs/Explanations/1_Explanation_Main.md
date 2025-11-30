## 🎓 Introduction

The *Imperial College London Thesis Submission Checklist* defines the essential requirements for the structure, contents, and presentation of a thesis, but it does **not prescribe a single fixed layout**.  
This gives candidates flexibility in how they design and typeset their work, provided that:

- All required elements are included.
- The order of elements follows the regulations given in the checklist.
- The document is clear, legible, and professionally presented.

This document serves four main purposes:

1. **Explain** the official requirements defined in the Thesis Submission Checklist and related Imperial College regulations.  
2. **Show** how each requirement has been implemented in this LaTeX template, by linking rules to specific code snippets.  
3. **Recommend good practice** in academic typesetting and document design.  
4. **Help you adapt the template** confidently while remaining compliant with Imperial’s rules.

By combining regulatory guidance with technical explanations, this document is intended to help you both **use** and **customise** the template responsibly.

---

## ⚙️ Document Settings — `\documentclass`  
*(Checklist: Presentation section)*

Every LaTeX document starts by declaring its **document class**, which determines the overall structure and many formatting defaults (chapters, sections, margins, floats, etc.).

In this template we use the following declaration:

<!-- SNIPPET: documentclass -->

This choice supports the Presentation requirements in the checklist (the **Presentation** section, which covers legibility, layout and margins) in several ways:

- The `book` class provides **chapters**, **front matter**, and **appendices**, matching the typical structure of a PhD thesis.
- A base font size of **11pt** gives good readability for a long document.
- The `twoside` option prepares a **double‑sided layout** (odd/even pages), which is standard for theses.
- The `openany` option allows chapters to begin on **any page**; if you prefer a more traditional layout where chapters always start on a right‑hand page, you can change this to `openright`.

In the Presentation section, the checklist states that **page content should be centred so that margins are equal‑distant from the edge of the page** and that main text should use **double or one‑and‑a‑half spacing**. The technical implementation of these rules is done in the **preamble**, described next.

---

## 🏛️ Preamble, Headers/Footers, and Title Page  
*(Checklist: Presentation + Title‑page requirements)*

The **preamble** collects all global formatting: packages, margins, page style, and other settings.  
This template loads `preamble.tex` and then configures:

- Headers and footers (page style).
- Page numbering.
- The title page.

The core code is:

<!-- SNIPPET: preamble_title -->

How this relates to specific checklist points:

- **Presentation section**:
  - The requirement that **page content is centred with symmetrical margins** is implemented in `preamble.tex` (geometry, layout, spacing).
  - The requirement for **double or one‑and‑a‑half line spacing** in the main text (with single spacing allowed for quotations or footnotes) is also enforced via settings in `preamble.tex`.

- **Page numbering** (Presentation section):
  - The checklist states that **all pages must be numbered in one continuous sequence in Arabic numerals from 1 onwards**, including the title page and all content (text, diagrams, blank pages, etc.).
  - The commands `\pagenumbering{arabic}` and `\setcounter{page}{1}` ensure that the **title page is page 1** and that numbering continues in Arabic numerals throughout.

- **Title page information** (Presentation section – title page bullet points):
  - The title page must include:
    - The **approved thesis title**.
    - The candidate’s **full name** (as registered).
    - “Imperial College London” and the **Department** name.
    - The **degree** (e.g. PhD, MPhil, EngD, MD(Res)).
  - These items are defined in `titlepage.tex`, which is loaded by this snippet.

Because these components are crucial for compliance, this template also provides **separate explanatory pages**:

- One document that explains **`preamble.tex`** in detail (packages, margins, spacing, fonts, headers/footers, and how these satisfy the Presentation requirements).
- One document that explains **`titlepage.tex`** and shows exactly how it fulfils the title‑page requirements in the checklist.

---

## 📄 Dedication (Optional – not required in checklist)

The *Thesis Submission Checklist* does **not** require a dedication page and does not assign it a section number. Its inclusion and position are therefore entirely optional and left to your judgement.

By convention, a dedication:

- Appears near the beginning of the thesis.
- Contains a brief personal statement.

This template provides a simple dedication page:

<!-- SNIPPET: dedication -->

You can:

- Replace the example text with your own dedication.
- Adjust the vertical spacing so that the text appears higher or lower on the page.

---

## 📜 Declaration of Originality  
*(Checklist: “Statement of Originality” section)*

The checklist contains a section titled **Statement of Originality**, which requires that:

- You include a **short statement in your own words** confirming that the thesis is your own work.
- You confirm that all other work is properly referenced.

This template implements that requirement with a dedicated Declaration of Originality page:

<!-- SNIPPET: Declaration of Originality -->

To comply with the **Statement of Originality** section:

- Replace `Your Name` with your full registered name.
- Ensure the wording clearly states that:
  - The thesis and the work it presents are your own, and
  - Any contributions from others or reused material are appropriately acknowledged.

This snippet also contains the **copyright statement** needed for the “Copyright Declaration” section of the checklist, because the thesis will be made available in the College’s repository.

---

## ©️ Copyright Declaration and Licence  
*(Checklist: “Copyright Declaration” section)*

The checklist’s **Copyright Declaration** section states that:

- As your thesis will be made available for public reference, you must include a **copyright statement** at the beginning.
- You may choose from any of the **Creative Commons licences** when publishing your thesis on Spiral.
- If no specific licence is required, the College recommends wording corresponding to a **Creative Commons Attribution‑Non Commercial 4.0 International Licence (CC BY‑NC 4.0)**.

In this template:

- The copyright wording in the **Declaration of Originality** snippet should:
  - Explicitly name the licence (e.g. “Creative Commons Attribution‑Non Commercial 4.0 International Licence (CC BY‑NC)”).
  - Explain that others may reuse the thesis under the conditions of that licence (e.g. non‑commercial use with attribution).

This directly addresses the requirements in the **Copyright Declaration** section of the checklist.

---

## 📑 Abstract — Checklist **§7.1**

Section **7.1** of the checklist (titled **Abstract**) states:

> “The title-page should be followed by an abstract consisting of no more than **300 words**.”

This template enforces the correct position and basic structure:

<!-- SNIPPET: Abstract -->

To comply with **§7.1**:

- Place the abstract immediately after the title page and declarations.
- Ensure it is **no longer than 300 words**.
- Summarise:
  - The research question or problem.
  - The methods used.
  - The main results.
  - The overall conclusion or significance.

LaTeX will not enforce the 300‑word limit automatically; you must check this yourself.

---

## 🙏 Acknowledgements  
*(Optional – not specified in a numbered section)*

The checklist does **not** give a numbered section for Acknowledgements and does not mandate them, but they are standard in PhD theses.

Typical content:

- Thanks to supervisors and co‑supervisors.
- Recognition of collaborators, technical/administrative staff.
- Acknowledgement of funding bodies and personal support (family, friends).

This template provides an unnumbered Acknowledgements chapter:

<!-- SNIPPET: Acknowledgements -->

Because the checklist does not specify its exact position, you may place this section:

- After the abstract and before the table of contents, or
- After the conclusion, depending on your department’s preference.

---

## 📣 Dissemination  
*(Optional – not specified in a numbered section)*

The checklist does not have a numbered section on **Dissemination**, but it can be very useful to record research outputs related to the thesis:

- Journal articles.
- Conference papers and posters.
- Preprints and technical reports.

This template includes an optional Dissemination chapter:

<!-- SNIPPET: Dissemination -->

You can:

- Replace the example items with your actual publications and outputs.
- Remove this section entirely if you prefer.

Since it is not part of a numbered requirement, its inclusion is purely optional.

---

## 📚 Nomenclature and Acronyms  
*(Optional – not specified in a numbered section)*

The checklist does not explicitly mention **nomenclature** or **lists of acronyms**, but they can significantly improve readability in technical or mathematical theses.

This template offers optional sections for both:

<!-- SNIPPET: Nomenclature_Acronyms -->

Usage:

- Use the **Nomenclature** section to define symbols, variables, and notation.
- Use the **Acronyms** section to list abbreviations and their meanings.

These sections are examples of good practice rather than formal checklist requirements.

---

## 📋 Contents, List of Figures, and List of Tables  
*(Checklist: “Table of Contents” — **§8.1**)*

Section **8.1** of the checklist (titled **Table of Contents**) states that:

> “The abstract should be followed by a full table of contents (including any additional material supplied separately to the main body of the thesis) and a list of tables, figures, photographs and any other materials.”

This template implements **§8.1** as follows:

<!-- SNIPPET: Contents, List of Figures/Tables -->

How this satisfies **§8.1**:

- `\tableofcontents` produces a **full table of contents** for the thesis, including chapters and sections.
- `\listoffigures` generates the **List of Figures**.
- `\listoftables` generates the **List of Tables**.

Together, these lists ensure that all major structural elements and visual materials are clearly indexed, as required by section **8.1**.

Notes on LaTeX behaviour:

- LaTeX writes the contents and lists to auxiliary files during compilation (`.toc`, `.lof`, `.lot`).
- You may need to compile the document at least **twice** for new headings, figures, or tables to appear with correct page numbers.

---

## 📘 Main Chapters  
*(Checklist: overall thesis structure)*

The checklist describes the overall structure of the thesis (title page, abstract, table of contents, main body, appendices, etc.), but it does **not enforce specific chapter titles** for the main body.

Typical PhD theses include:

- **Introduction** — context and aims.
- **Related Work / Literature Review**.
- **Methods / Materials and Methods**.
- **Results**.
- **Discussion**.
- **Conclusion**.

This template provides a representative main‑chapter structure:

<!-- SNIPPET: CHAPTERS -->

Each chapter is in a separate file under `chapters/`, which keeps the main document manageable and makes it easy to rearrange or extend the structure while staying consistent with the overall framework implied by the checklist.

---

## 📎 Appendices — Checklist **§9.1**

Section **9.1** of the checklist (titled **Appendices**) states that:

- Appendices should be placed **at the end of the thesis after the bibliography**.
- They should include:
  - Any data that examiners may wish to refer to, but will not examine in detail.
  - Copies of **permission documents** showing that you have permission to reproduce third‑party copyrighted material (papers, images, figures, maps, etc.).

This template implements **§9.1** as follows:

<!-- SNIPPET: APPENDIX -->

To comply with **§9.1**:

- Place all appendices **after** the bibliography in the final document.
- Use appendix chapters (e.g. *Appendix A*, *Appendix B*, etc.) to:
  - Store supplementary data, extended tables or figures.
  - Include scanned or textual copies of permission letters and licences for third‑party material used in the thesis.

---

## 📖 Bibliography (Required – linked to overall structure and **§8.1**)

The checklist expects a **complete bibliography** of works cited in the thesis.  
Although the section you provided numbers **§7.1** for the abstract and **§8.1** for the table of contents, it does not give a separate numbered heading labelled “Bibliography”. Instead, the requirement for a bibliography forms part of the **overall thesis structure**, in which:

- The abstract is followed by the table of contents and lists (**§8.1**).
- The **main body** and **references/bibliography** then appear.
- Appendices follow **after** the bibliography (**§9.1**).

This template uses BibLaTeX to generate the bibliography:

<!-- SNIPPET: Bibliography -->

In practice, this satisfies the checklist’s expectation that:

- All sources cited in the thesis are collected in a **full bibliography**.
- The bibliography appears **before** the appendices (as implied by **§9.1**, which explicitly says appendices come at the end *after* the bibliography).

To use this correctly:

- Maintain references in one or more `.bib` files.
- Configure the citation style in `preamble.tex` to match your discipline and any departmental guidance (e.g. numeric, Harvard, Vancouver).
- Run the LaTeX ➝ Biber/BibTeX ➝ LaTeX compile cycle so that all citations and bibliography entries are resolved.

---

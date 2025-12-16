<!-- Imperial College London PhD Thesis Template README -->

# 📘 Imperial College London PhD Thesis LaTeX Template

This repository provides a **LaTeX template** designed for preparing and formatting a **PhD Thesis at Imperial College London**.  
The template ensures **full compliance with Imperial College’s official thesis formatting guidelines**, while offering a **clear, modern, and modular structure** that supports ease of use and long-term maintainability.

![Imperial Thesis Template Preview](docs/assets/Cover.png)

---

### 👥 Authors & Acknowledgements

This exemplar was developed at **Imperial College London** by:

- **João Graça Gomes**  - PhD Candidate, Dyson School of Design Engineering
- **Dr. Chris Cooling** – Senior Teaching Fellow, Early Career Researcher Institute  
- **Diego Alonso Alvarez** – Head of Research Software Engineering, ICT, Central Faculty  

---

## 🎓 Learning Outcomes

The main objective of this project is to develop a **standardized, user-friendly LaTeX template** that:

1. **Conforms strictly** to Imperial College London’s thesis presentation regulations and formatting requirements.  
2. **Facilitates consistency** in typography, structure, and referencing across departments and research groups.  
3. **Simplifies the writing process** for postgraduate researchers by providing pre-defined environments for chapters, sections, figures, tables, and appendices.  
4. **Integrates best practices** in academic writing, including compatibility with BibLaTeX for references and packages for mathematical typesetting, graphics, and indexing.  
5. **Ensures long-term maintainability**, with modular configuration files (e.g., `preamble.tex`, `settings.tex`) for easy customization.  

---

## 🎯 Target Audience

This LaTeX template is designed primarily for **postgraduate researchers** preparing their **Doctor of Philosophy (PhD)** theses at **Imperial College London**, but it can also benefit a broader academic audience.

### The following groups will find this exemplar particularly useful:

#### 1. PhD Candidates at Imperial College London
- Students seeking a compliant, ready-to-use LaTeX framework that meets official thesis formatting regulations.  
- Researchers aiming to produce a professional and consistent document for both printed and electronic submission.  

#### 2. Supervisors and Research Advisors
- Academics who wish to provide their students with a standardised, institutionally aligned thesis format.  
- Supervisors reviewing draft theses who value a consistent structure for efficient feedback.  

#### 3. Departmental Administrators and Graduate Schools
- Departments interested in maintaining uniformity in the presentation of theses across research groups.  
- Administrative teams developing departmental LaTeX templates derived from this core structure.  

#### 4. Postgraduate Researchers from Other Institutions
- Scholars from other universities looking for a high-quality exemplar of a compliant UK-style PhD thesis format.  
- Researchers who wish to adapt Imperial’s clear, modular structure for their own institutional guidelines.  

---

## ✅ Prerequisites

### 📚 Academic
- Familiarity with **LaTeX** and basic document compilation workflows.  
- Understanding of **academic writing conventions** and thesis structure (chapters, abstracts, references, appendices).  
- Optional: Experience with **BibLaTeX**, **Biber**, and reference management tools (e.g., Zotero, Mendeley).  

### 💻 System

You can work either locally or directly in Overleaf — choose the workflow that suits you best.

- Option A — Overleaf (no local installation required):
  - Use **Overleaf** to compile and manage your thesis online.
  - Import the project via “New Project → Import from GitHub” or “New Project → Upload Project” (ZIP).
  - In Project Settings, set **Compiler** to **XeLaTeX** or **LuaLaTeX**.
  - If using **BibLaTeX**, set **Bibliography tool** to **Biber**.
  - Note: Overleaf project size and quota limits depend on your plan.

- Option B — Local setup:
  - Install a **LaTeX distribution**: [TeX Live](https://www.tug.org/texlive/), [MiKTeX](https://miktex.org/), or [MacTeX](https://www.tug.org/mactex/).
  - Recommended compiler: **XeLaTeX** or **LuaLaTeX** (for Unicode and modern font support).
  - Ensure **Biber** is installed if you use **BibLaTeX**.
  - Compatible with **TeXstudio**, **VS Code (LaTeX Workshop)**, or any LaTeX IDE.
  - Minimum **5 GB free disk space** for LaTeX and auxiliary files.

---

## 🚀 Getting Started

Follow these steps to begin using the Imperial College London PhD Thesis Template:

1. Choose your workflow:
   - Overleaf:
     - Open Overleaf → New Project → Import from GitHub (or Upload Project ZIP).
     - In Project Settings, set Compiler to **XeLaTeX** or **LuaLaTeX**.
     - If using **BibLaTeX**, set Bibliography tool to **Biber**.
     - Click **Recompile** and start editing files (e.g., `preamble.tex`, `settings.tex`, `chapters/`).
   - Local:
     - Clone the repository:
       ```bash
       git clone https://github.com/your-username/imperial-thesis-template.git
       ```
     - The LaTeX source files are found in the [phd-thesis](https://github.com/ImperialCollegeLondon/ReCoDE-LaTeX-PhD-Template/tree/main/phd-thesis) directory. Open the directory in your IDE and compile (example):
       ```bash
       latexmk -pdf -xelatex main.tex
       ```
       or
       ```bash
       latexmk -pdf -lualatex main.tex
       ```
     - Ensure **Biber** runs for references (BibLaTeX workflow).

<!-- LICENCE.
Imperial prefers BSD-3. Please update the LICENSE.md file with the current year.
-->
## Licence 📄

This project is licensed under the [BSD-3-Clause license](LICENSE.md).

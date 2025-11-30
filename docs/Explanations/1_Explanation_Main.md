## 🎓 Introduction

The *Imperial College London Thesis Submission Checklist* outlines the essential requirements for PhD thesis formatting and structure, but it does **not provide strict or exhaustive layout specifications**.  
This leaves flexibility for candidates to decide how to design and typeset their thesis, as long as the document contains all required elements in the correct order. TEST!

This document serves four main purposes:

1. **Explain** the official requirements defined in the Thesis Submission Checklist and related Imperial College regulations.  
2. **Demonstrate** how each requirement has been implemented in this LaTeX template — linking each rule to the corresponding code snippet or environment.  
3. **Recommend best practices** in academic typesetting, presentation, and structure to help produce a professional-quality thesis.  
4. **Empower users** to understand the reasoning behind each implementation so they can confidently make their own adjustments while remaining compliant with Imperial College’s regulations.

By combining regulatory guidance with technical explanations, this document helps PhD students not only use the provided template effectively but also **customize it responsibly**, ensuring their thesis remains compliant, well-formatted, and professionally presented.

## ⚙️ Document Settings

Every LaTeX document begins by declaring its **class** , this determines the overall structure, formatting, and layout rules used by the compiler.  
For this thesis template, the following declaration is used:

```markdown
  ```latex
\documentclass[11pt, twoside, openany]{book} 
% 'book' provides chapters, front matter, ZZZ appendices and a well-structured layout suitable for theses.
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
```


### 🏛️ Title Page — Compliance with Imperial College Thesis Submission Checklist (§ 4.5)

According to the *Imperial College London Thesis Submission Checklist* (Section 4.5),  
the title page **must include** the following information:

> - The approved title of the thesis (as confirmed at the point of examination entry)  
> - The candidate’s full name, as registered at the College  
> - *Imperial College London* and the name of the Department  
> - The degree for which the thesis is submitted (e.g. PhD)

```latex
\begin{titlepage}                  % Creates a dedicated title page environment (standard LaTeX feature).

### 📄 Abstract Section — Compliance with Imperial College Thesis Submission Checklist (§ 7.1)

According to the *Imperial College London Thesis Submission Checklist* (section 7.1):

> “The title page should be followed by an abstract consisting of no more than 300 words.”

This template fully complies with that requirement.

The **Abstract** is defined in the file as:

```latex
\chapter*{Abstract} %For unnumbered chapters use the "*" after chapter e.g. (\chapter*{...}).
\addcontentsline{toc}{chapter}{Abstract} %{toc} adds this entry to the Table of Contents.
% Write your abstract here (maximum 300 words)
```

# Dedication
The *Imperial College London Thesis Submission Checklist* does **not require** a Dedication page. Including one is **entirely optional**. By convention, **Dedications usually appear at the very beginning of a thesis**, before the Abstract. However, there is no strict rule, so you can position it differently if desired.  

---

```latex
\cleardoublepage       %Ends the current page and starts a new one, ensuring that the next content begins on a right-hand (odd-numbered)
\thispagestyle{empty}  % Removes page numbers and headers/footers.
\vspace*{5cm}          % Adds vertical space to position the dedication text. Regular \vspace{5cm} might not work at the top of a page, because LaTeX can ignore vertical space there. \vspace*{5cm} forces LaTeX to apply the space even at the top of a page, which is exactly what you want for a dedication page. Adjustable: You can change 5cm to any value (e.g., 3cm, 7cm) depending on how far down you want the dedication text to appear.
\begin{center}
    \emph{To my family,\\
    and friends.}       % Replace with your personal dedication text.
\end{center}
\cleardoublepage       % Starts the next content on a right-hand page.
```

### Acknowledgements

The *Imperial College London Thesis Submission Checklist* does **not set rules** for the Acknowledgements section.  Despite being **fully optional**, including it is **common academic practice** and expected in most PhD theses.  This section allows the author to express gratitude to supervisors, collaborators, funding bodies, friends, and family.

By convention, **Acknowledgements are placed after the Abstract and before the Table of Contents**, although Imperial does not mandate a fixed position. If you prefer the Acknowledgements to appear in a different place, for example, after the Conclusion,
you can simply cut and paste the Acknowledgements block to that position in the document.

---

#### 🧩 LaTeX Structure

```latex
\chapter*{Acknowledgements} % Creates an unnumbered "Acknowledgements" section. 
\addcontentsline{toc}{chapter}{Acknowledgements} % Adds "Acknowledgements" to the Table of Contents manually. 
% Write your acknowledgements text here.          % Insert personal or professional acknowledgements.
```



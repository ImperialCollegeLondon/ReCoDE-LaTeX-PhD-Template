## Appendices, Code, and Other Supporting Material 📎

This page explains how to use **appendices** in your thesis, including how to include **code listings**, **illustrative material**, and **supporting documentation**. The aim is to help you use the template in a way that is both practical and consistent with the **Imperial College thesis checklist**.

According to the checklist (Section 9), appendices should come **after the bibliography** and contain material that examiners may wish to refer to, but that they will not examine in detail. Think of appendices as a place for **evidence, examples, and supplementary detail**, not as an extension of the main argument.

---

### 1. Role of appendices (Checklist §9)

Section 9 of the Imperial checklist emphasises that appendices should be at the **end of the thesis** and may include:

- Data that examiners may want to see, but will *not* examine line‑by‑line.
- Documentation such as **permission letters** to reproduce third‑party material.
- Additional plots, tables, or technical details that would clutter the main chapters.

Good candidates for appendices include:

- Extended results, raw data samples, or additional figures.
- Long derivations, proofs, or technical specifications.
- Code listings and configuration files that illustrate how your methods were implemented.

Appendices should be **labelled and structured clearly** (e.g. Appendix A, B, C), and cross‑referenced from the main text where relevant.

---

### 2. Code examples in appendices

The template includes an example of a **Python code snippet** in Appendix A, typeset using the `minted` environment for syntax highlighting. This demonstrates how to present small, readable code fragments that support your methods. Remember adding code to your thesis or appendix is entirely **optional**.

Short code listings in an appendix are useful when you want to:

- Show a **minimal working example** of an algorithm described in the main text.
- Illustrate how a key formula or method is implemented in practice.
- Provide enough detail for interested readers to understand or reproduce your work, without overloading the main chapters.

To compile `minted` environments, you must enable **shell‑escape** in your LaTeX compiler (e.g. via project settings in Overleaf or using the `-shell-escape` flag with `latexmk`).

<!-- SNIPPET: code_pythagoras -->
```latex
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

---

### 3. Illustrative material and additional files (Checklist §10)

Section 10 of the checklist covers **illustrative material** provided alongside the thesis (e.g. videos, large datasets, software, or other digital artefacts). Key points:

- Additional illustrative material may need to be submitted to the **Registry Assessment Records Team** via the channels specified (e.g. email or upload).
- Such material should be **clearly referenced** in your thesis, with a short description of what it is and how it relates to your work.
- Where possible, you should provide **stable access** (e.g. DOIs, repository links) and follow any departmental or funder data‑sharing policies.

In practice, your thesis might:

- Mention that **source code, full datasets, or interactive notebooks** are available in a repository, and
- Use the appendices to briefly explain what is in those external resources and how an examiner could use them.

---

### 4. Copyright, plagiarism, and permissions (Checklist §11)

Section 11 of the checklist is crucial for any material in your appendices (figures, tables, code, documents):

- Your thesis must **not contain plagiarism**, including copying code, text, or figures without proper attribution.
- You must have **permission** to reproduce any third‑party material (papers, images, figures, maps, code, etc.), including within the appendices.
- You must comply with any **sponsorship, confidentiality, or intellectual property** obligations (for example, if your work is industrially sponsored or contains sensitive data).

The checklist also specifies that you should include copies of **permission documents** in the appendices, so examiners can verify that you are allowed to reuse all third‑party material included in the thesis.

---

### 5. Practical recommendations

When using appendices for code, illustrative material, and documentation:

- Keep the **main thesis self‑contained**: the core argument and results should be understandable without reading every line of the appendix.
- Use appendices for **supporting detail**: extended methods, extra figures, long tables, code snippets, sample data, and permission letters.
- Make sure everything in the appendices is:
  - **Clearly labelled** (appendix titles, section headings, captions),
  - **Referenced from the main text** where relevant (e.g. “see Appendix A for code listing”), and
  - **Ethically and legally compliant** with the Imperial checklist (Sections 9–11).

For any specific questions about what your appendices should or should not contain, always:

- Re‑read the **Imperial thesis checklist**, and  
- Confirm with your **supervisor or departmental admin** whether your programme has any additional requirements.

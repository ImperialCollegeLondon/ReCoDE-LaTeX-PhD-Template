## Tables Explanation 📋

This page explains how to structure and format tables in your thesis, using examples from a typical **Related Work** or **Results** chapter. The aim is to provide reusable, compliant layouts rather than to dictate your scientific content.

From an Imperial College checklist perspective, tables must be:

- **Clearly readable**: appropriate font size, no overcrowded cells, and good use of spacing.
- **Numbered and captioned** consistently (Table 2.1, 2.2, …).
- **Referenced in the text**: every table should be mentioned and explained, not just left “floating”.
- **Properly titled for the List of Tables** using short, descriptive captions.

### Why tables?

Tables are ideal when you need to present:

- **Structured comparisons** (e.g. methods, datasets, performance metrics).
- **Parameter lists** (e.g. variables, units, default values).
- **Categorical summaries** (e.g. related work, design options, case studies).

They are often used in the **Related Work** chapter because they allow you to condense a large body of literature into a clear, scannable format.

---

### 3×3 example table

As shown in Table `example_3x3`, a simple $3 \times 3$ layout is useful for compact relationships or for comparing a small set of variables.

Key ideas illustrated by this template:

- The **caption** clearly states what the table contains: parameters X, Y, and Z.
- The optional **short caption** (`[3×3 Example Table]`) defines the entry in the *List of Tables*.
- Column alignment (`l c r`) is used to control how text and numbers are positioned:
  - $l$ for left‑aligned labels,
  - $c$ for centred columns,
  - $r$ for right‑aligned numerical values.

<!-- SNIPPET: tables_3x3 -->
```latex
\begin{table}[h!]
    \centering
    % The optional caption [short title] defines what appears in the List of Tables.
    \caption[3×3 Example Table]{A 3×3 table template with parameters X, Y, and Z.}
    \label{tab:example_3x3}
    \begin{tabular}{l c r} 
        % l = left aligned, c = centred, r = right aligned
        \toprule
        Parameter & Value & Units \\
        \midrule
        X1 & 10 & m \\
        X2 & 20 & m \\
        X3 & 30 & m \\
        \bottomrule
    \end{tabular}
\end{table}
```

---

### 5‑column example table

Table `example_5col` shows a 5‑column layout suitable for **experimental outputs**, benchmarking results, or design specifications. It can be easily extended to more rows or columns as needed.

Key ideas illustrated by this template:

- A mix of alignments (`l c c c c r`) separates **labels** (left‑aligned) from **numeric results** (right‑aligned), which improves readability.
- The structure is flexible: you can replace placeholder entries (`--`) with your own measurements, metrics, or categories.
- The caption explicitly describes what the table represents (e.g. parameters A–E for different samples).

<!-- SNIPPET: tables_5col -->
```latex
\begin{table}[h!]
    \centering
    \caption[5-column Example Table]{A 5-column table template suitable for experimental results or design specifications with parameters A–E.}
    \label{tab:example_5col}
    \begin{tabular}{l c c c c r}
        % lccccr layout:
        % l = sample name left aligned
        % c = four columns centred
        % r = final column right-aligned (useful for numerical data)
        \toprule
        Sample & A & B & C & D & E \\
        \midrule
        1 & -- & -- & -- & -- & -- \\
        2 & -- & -- & -- & -- & -- \\
        3 & -- & -- & -- & -- & -- \\
        \bottomrule
    \end{tabular}
\end{table}
```

---

### Checklist‑aligned good practice for tables

In order to stay in line with the Imperial thesis checklist, you should ensure that:

- Each table has a **clear, descriptive caption** that explains what is being shown.
- Tables are **numbered consistently** within each chapter (and, if needed, across the thesis).
- Every table is **referenced from the main text** (e.g. “see Table 3.2”) and is **interpreted**—you should tell the reader what they should notice in the table.
- Units and symbols are **defined** somewhere (in the table headings, footnotes, or surrounding text), so the reader is not left guessing.

Used well, tables make it much easier for examiners to understand your results and for your writing to meet both the **clarity** and **presentation** expectations in the Imperial guidelines.

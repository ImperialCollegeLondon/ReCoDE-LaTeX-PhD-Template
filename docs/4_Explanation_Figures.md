## Figures Explanation 📊

This page explains how to structure and use **multi‑panel figures**, as an example, in the results chapter of your thesis. The goal is not to dictate your scientific content, but to give you reusable patterns for presenting it clearly and consistently.
From an Imperial College compliance perspective, figures must be **clearly legible, consistently formatted, and properly referenced** in the text. The checklist also expects that all figures are numbered in a single logical sequence (Figure 1.1, 1.2, …) and that each one has a **descriptive caption** and is actually **discussed in the main text**, rather than left unexplained.

### Why multi‑panel figures?

A dedicated results chapter is standard in most thesis formats. In this chapter, figures often do the heavy lifting: they communicate **trends, comparisons, and patterns** more efficiently than paragraphs of text. Multi‑panel figures:

- Allow you to **compare multiple conditions** or time points in one place.
- Help the reader see **relationships and progressions** at a glance.
- Reduce the need for separate, repetitive single‑panel figures.

### 2×2 multi‑panel figure (four panels)

The first example (Figure `four_panels`) uses a $$2 \times 2$$ layout (panels a–d). This is a good pattern when:

- You have **four related scenarios** (e.g. different parameter settings, methods, or time points).
- You want a **single caption** that explains how the panels relate.
- You need a concise visual summary instead of four separate figures.

Key ideas illustrated by this template:

- Each subfigure has its own **caption** and **label**, so you can reference them individually (a, b, c, d).
- The overall **figure caption** explains what the four panels show collectively.
- You can cite the source of the data or images in the caption (e.g. `\cite{Gomes2022}`).

<!-- SNIPPET: figures_four -->
```latex
\begin{figure}[h!]
    \centering

    % -------------------
    % Row 1
    % -------------------
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 0.png}
        \caption{Image a}
        \label{fig:sub_a}
    \end{subfigure}%
    \hfill
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 1.png}
        \caption{Image b}
        \label{fig:sub_b}
    \end{subfigure}
    

    % -------------------
    % Row 2
    % -------------------
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 2.png}
        \caption{Image c}
        \label{fig:sub_c}
    \end{subfigure}%
    \hfill
    \begin{subfigure}[b]{0.4\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 5.png}
        \caption{Image d}
        \label{fig:sub_d}
    \end{subfigure}

    % -------------------
    % Overall caption 
    % -------------------
    \caption[Four-panel figure]{Four-panel figure showing different aspects of the experiment.  
    Subfigures a–d correspond to distinct experimental conditions or processing steps.}
    \label{fig:four_panels}
\end{figure}
```

### Two‑panel figure (side‑by‑side)

The second example (Figure `two_panels`) shows a **side‑by‑side two‑panel** layout. This is suitable when:

- You want to compare **two conditions** directly (e.g. baseline vs. proposed method).
- The reader needs to see **differences or improvements** at a glance.
- You want a cleaner layout than stacking two separate full‑width figures.

<!-- SNIPPET: figures_two -->
```latex
\begin{figure}[h!]
    \centering

    % Panel a (left)
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 5.png}
        \caption{Description of image a}
        \label{fig:sub_a1}
    \end{subfigure}
    \hfill
    % Panel b (right)
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{phd-thesis/figures/Picture 2.png}
        \caption{Description of image b}
        \label{fig:sub_b1}
    \end{subfigure}

    \caption[Two-panel figure]{Two-panel figure comparing condition a) and condition b).}
    \label{fig:two_panels}
\end{figure}
```

Key ideas illustrated:

- Both panels share the same **y‑axis or visual scale**, making comparisons fair and readable.
- Using widths like $$0.48\textwidth$$ places both panels across the page with minimal wasted space.
- Subfigure labels (e.g. `\ref{fig:sub_a1}`) let you refer to specific panels in the text.

### How to adapt these templates

When you use these examples in your own thesis:

- **Replace the image files** with your own plots or diagrams.
- **Update captions** to describe your actual experiment and results.
- **Keep labels meaningful** (e.g. `fig:results_accuracy_a`) so cross‑references are easy to manage.
- Ensure each figure **adds information** and is referenced in the main text—avoid decorative or unexplained figures.

---





## Equations Explanation 🧮

This page explains how to typeset mathematical equations in LaTeX using a simple but common example: the **sample mean** and **sample standard deviation**. The goal is to show you how to write clear, well‑formatted equations that can be referenced in your thesis text.

The [Theses for Imperial College Research Degrees](https://www.imperial.ac.uk/media/imperial-college/administration-and-support-services/registry/academic-governance/public/academic-policy/research-degree-examinations/Thesis-Submission-Checklist.pdf) states that equations must be:

- **Legible and consistently formatted** (same fonts, sizes, and spacing).
- **Numbered systematically** when referred to in the text.
- **Explained in words**: you should never drop an equation into the thesis without telling the reader what it means and how it is used.

### Why show this example?

In many experimental analyses, you need to quantify how variable your measurements are. The **sample mean** and **sample standard deviation** are standard tools across engineering, science, and data analysis. They are also a good example of:

- Using LaTeX environments like `equation` for numbered display equations.
- Using inline math for symbols inside sentences.
- Referencing equations consistently in your text.

### Sample standard deviation

For a sample of $n$ observations $x_1, x_2, \dots, x_n$, the **sample standard deviation** $s$ measures how spread out the data are from the mean. In this example, Equation std_sample shows that the standard deviation increases as the data points deviate further from the sample mean. This form is widely used when analysing repeated measurements, sensor data, or experimental uncertainty.

<!-- SNIPPET: equations_std -->
```latex
\begin{equation}
    s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} \left(x_i - \bar{x}\right)^2 }
    \label{eq:std_sample}
\end{equation}

% Explanation:
% - The equation environment automatically numbers the equation.
% - \sum creates the summation symbol.
% - \bar{x} denotes the sample mean.
% - Use \label to refer to the equation later in the text.
```

### Sample mean

The sample mean $\bar{x}$ is the average of the observations and is used inside the expression for the standard deviation.

<!-- SNIPPET: equations_mean -->
```latex
\begin{equation}
    \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
    \label{eq:mean_sample}
\end{equation}
```

### Connecting back to the text and checklist

In a thesis that follows the Imperial guidelines, each equation should:

- Be **numbered** if you need to refer to it later (e.g. “see Equation (4.2)”).
- Be **introduced and explained** in complete sentences (what does each symbol mean? what is the purpose of this equation?).
- Be **used** in your discussion of methods or results, not left floating without context.

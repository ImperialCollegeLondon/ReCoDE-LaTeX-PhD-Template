## Code 📎

The template includes an example of a **Python code snippet** in Appendix A, typeset using the `minted` environment for syntax highlighting. This demonstrates how to present small, readable code fragments that support your methods. Remember adding code to your thesis or appendix is entirely **optional**.

Short code listings in an appendix are useful when you want to:

- Show a **minimal working example** of an algorithm described in the main text.
- Illustrate how a key formula or method is implemented in practice.
- Provide enough detail for interested readers to understand or reproduce your work. Placing this is in an appendix will avoid it cluttering the main chapters.

To compile `minted` environments, you must use the `minted` package and enable **shell‑escape** in your LaTeX compiler (e.g. via project settings in Overleaf or using the `-shell-escape` flag with `latexmk`).

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

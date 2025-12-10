## Title Page Explanation 🎓

This page explains the structure and purpose of the custom title page used in the PhD thesis template for Imperial College London. Each element is annotated to clarify whether it is **mandatory**, **recommended**, or **purely stylistic**.

### Page numbering (Checklist Section 4.4)

Section 4.4 of the official checklist emphasizes that **all pages must be numbered in one continuous sequence**, from the title page to the last page of text, in **Arabic numerals starting at 1**. This sequence must include *everything* in the document: maps, diagrams, blank pages, etc.

A lot of students forget to number the very first page, treating it as a separate “cover”. Regardless of your aesthetic preferences, the checklist is quite clear on this point: **the title page is page 1** (yes, even if it ruins your minimalist designer soul).

### Required information on the title page (Checklist Section 4.5)

Section 4.5 specifies that the title page **must** include:

- The **approved title** of the thesis (as confirmed at examination entry)
- The **candidate’s full name**, as registered at the College
- **Imperial College London** and the **name of the Department**
- The **degree** for which the thesis is submitted (e.g. PhD)

The checklist does not explicitly require that you list your supervisors, but it is good practice to include their names and affiliations. This is optional and ultimately your decision.

---

<!-- SNIPPET: titlepage -->
```latex
\begin{titlepage}
\thispagestyle{fancy}               % Ensures the page number appears on the title page 
                                    % (required by Section 4.3).

  \centering                        % Centers the entire title page horizontally.

  \vspace*{-3cm}                    % Moves the whole block upwards.
                                    % To adjust vertical positioning of the page header,
                                    % change the value (e.g., -2cm, -1cm, 0cm).

  % -------------------------------
  % Institution Name
  % -------------------------------
  {\Large                           % Controls the font size of the entire block below.
                                    % Try \large, \LARGE, or \Huge if needed.
    {\fontsize{16pt}{18pt}\selectfont I}MPERIAL 
    {\fontsize{16pt}{18pt}\selectfont C}OLLEGE 
    {\fontsize{16pt}{18pt}\selectfont L}ONDON\par
  }
                                    % To adjust the size of the first capital letter only,
                                    % modify the 16pt (font size) and 18pt (baseline spacing).

  \vspace{0.5cm}                    % Adjust spacing between “Imperial College London”
                                    % and the School/Institute name.

  % -------------------------------
  % Department / School Name
  % -------------------------------
  {\large                           % Base font size for the school name.
    {\fontsize{14pt}{16pt}\selectfont E}ARLY
    {\fontsize{14pt}{16pt}\selectfont C}AREER
    {\fontsize{14pt}{16pt}\selectfont R}ESEARCHER 
    {\fontsize{14pt}{16pt}\selectfont I}NSTITUTE\par
  }
                                    % To change to your own department, simply replace
                                    % the text inside the braces.

  \vspace{6cm}                      % Vertical gap before the main title.
                                    % Increase or decrease to reposition the title block.

  % -------------------------------
  % Thesis Title Block
  % -------------------------------
  \rule{\linewidth}{1pt}            % Horizontal line above the title.
                                    % To change thickness, modify '1pt'.
                                    % To shorten the line, use 0.8\linewidth, etc.

  \vspace{0.3cm}

  {\huge\bfseries                   % Main thesis title block.
                                    % Adjust with \Huge, \LARGE, or remove \bfseries for non-bold.
    PhD Thesis Template\\
    An Example to Work On\par
  }

  \vspace{0.3cm}

  \rule{\linewidth}{1pt}            % Matching line beneath the title.
                                    % Mirrors the line above for symmetry.

  \vspace{0.3cm}

  % -------------------------------
  % Degree Name
  % -------------------------------
  {\Large
    {\fontsize{16pt}{18pt}\selectfont P}H%
    {\fontsize{16pt}{18pt}\selectfont D}~
    {\fontsize{16pt}{18pt}\selectfont T}hesis\par
  }
                                    % You can adjust the way “PhD Thesis” appears by
                                    % modifying the font size or removing spacing.

  \vspace{1cm}

  % -------------------------------
  % Candidate Name
  % -------------------------------
  {\Large João Graça Gomes\par}     % Replace with your full registered name.
                                    % Keep the size consistent with Imperial style.

  \vspace{1cm}

  % -------------------------------
  % Supervisor List
  % -------------------------------
  \begin{flushleft}
    \textit{Supervisors:}\\[0.3cm]  % Edit the label or remove if not needed.
  \end{flushleft}

  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} l r @{}}
    Dr Diego {\fontsize{14pt}{16pt}\selectfont A}{\textsc{LVAREZ}} & Early Career Researcher Institute\\
    Dr Chris {\fontsize{14pt}{16pt}\selectfont C}{\textsc{OOLING}} & Early Career Researcher Institute\\
  \end{tabular*}
                                    % Left column: supervisor names.
                                    % Right column: affiliations.
                                    % Add more lines as needed by copying the pattern.

  % -------------------------------
  % Submission Date
  % -------------------------------
  \vfill                             % Pushes the date to the bottom of the page automatically.

  \today                             % Automatically inserts today’s date.
                                     % Replace with your official submission date if preferred.

\end{titlepage}
```
```latex
(placeholder – will be replaced by the script)

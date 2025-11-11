# **Title Page Explanation**

This page explains the structure and purpose of the custom title page used in the thesis template for Imperial College London, Dyson School of Design Engineering.
Each element is annotated to clarify whether it is mandatory, recommended, or purely stylistic.

```latex
\begin{titlepage}
\thispagestyle{fancy}               % Ensures the page number appears (custom request).
                                    % Uses the fancy page style defined in the main file.

  \centering                        % Centers the whole layout horizontally.
                                    % Recommended for a clean, balanced title page.

  \vspace*{-3cm}                    % Moves the content upward by 3 cm.
                                    % Purely stylistic: used to visually balance the logo area.

  % -------------------------------
  % Imperial College London Header
  % -------------------------------
  {\Large
    {\fontsize{16pt}{18pt}\selectfont I}MPERIAL 
    {\fontsize{16pt}{18pt}\selectfont C}OLLEGE 
    {\fontsize{16pt}{18pt}\selectfont L}ONDON\par
  }
                                    % Mandatory: full institution name must appear.
                                    % Custom typography: capital first letter with small caps style.

  \vspace{0.5cm}

  % -------------------------------
  % Dyson School / Department Name
  % -------------------------------
  {\large
    {\fontsize{14pt}{16pt}\selectfont D}YSON 
    {\fontsize{14pt}{16pt}\selectfont S}CHOOL 
    OF
    {\fontsize{14pt}{16pt}\selectfont D}ESIGN 
    {\fontsize{14pt}{16pt}\selectfont E}NGINEERING\par
  }
                                    % Mandatory: must display your registered Department or School.
                                    % Here: Dyson School of Design Engineering.

  \vspace{6cm}                      % Large vertical spacing to separate header from the title block.
                                    % Recommended: provides strong visual hierarchy.

  % -------------------------------
  % Thesis Title Block (with lines)
  % -------------------------------
  \rule{\linewidth}{1pt}            % Decorative horizontal rule above the title.
                                    % Optional visual enhancement.

  \vspace{0.3cm}

  {\huge\bfseries
    PhD Thesis Template\\
    An Example to Work On\par       % Replace with your actual approved thesis title.
  }
                                    % Mandatory: official thesis title.
                                    % Recommended: use \huge and \bfseries for emphasis.

  \vspace{0.3cm}
  \rule{\linewidth}{1pt}            % Matching rule below the title for symmetry.

  \vspace{0.3cm}

  % -------------------------------
  % Degree Name
  % -------------------------------
  {\Large
    {\fontsize{16pt}{18pt}\selectfont P}H%
    {\fontsize{16pt}{18pt}\selectfont D}~
    {\fontsize{16pt}{18pt}\selectfont T}hesis\par
  }
                                    % Mandatory: must clearly state the qualification.
                                    % Stylised format matches the rest of the page.

  \vspace{1cm}

  % -------------------------------
  % Candidate Name
  % -------------------------------
  {\Large Jo\~{a}o Graça Gomes\par}
                                    % Mandatory: candidate's full registered name.

  \vspace{1cm}

  % -------------------------------
  % Supervisor List
  % -------------------------------
  \begin{flushleft}
    \textit{Supervisors:}\\[0.3cm]
  \end{flushleft}
                                    % Optional header label for clarity.

  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}} l r @{}}
    Professor John {\fontsize{14pt}{16pt}\selectfont C}{\textsc{ONNOR}} & Mechanical Engineering\\
    Dr. Winston {\fontsize{14pt}{16pt}\selectfont S}{\textsc{MITH}}     & Chemical Engineering\\
    Mr. Bernard {\fontsize{14pt}{16pt}\selectfont M}{\textsc{ARX}}      & Energy Futures Lab\\
  \end{tabular*}
                                    % Optional but strongly recommended for readability.
                                    % Right column lists affiliations.

  % -------------------------------
  % Submission Date
  % -------------------------------
  \vfill                             % Pushes the date to the bottom of the page.
                                    % Recommended for balanced layout.

  \today                             % Compilation date.
                                    % Optional: may replace with official submission date.

\end{titlepage}
```

# **📄Title Page Explanation**

This page explains the structure and purpose of the custom title page used in the PhD thesis template for Imperial College London.
Each element is annotated to clarify whether it is mandatory, recommended, or purely stylistic.

```latex
\begin{titlepage}
\thispagestyle{fancy}               % The title page MUST display a page number.
                                    % This follows Theses for Imperial College Research Degrees Checklist
                                    % Point 4.4, which states that all pages must
                                    % be numbered in one continuous sequence, i.e. from the title page
                                    % to the last page of type, in Arabic numerals from 1 onwards.
                                    %This sequence must include everything included in the document,
                                    % including maps, diagrams, blank pages, etc. 
                                    % Applying the'fancy' page style ensures the required footer with
                                    % the page number is present on the title page.

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
                                    % Mandatory: full institution name must appear. Point 4.5 of the Checklist.
                                    % Custom typography: capital first letter with small caps style. Can be modified according to the student choice.

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
                                    % Mandatory: must display your registered Department or School (point 4.5)
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
                                    % Mandatory: official thesis title. (point 4.5)
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
                                    % Mandatory: candidate's full registered name. (point 4.5)

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
                                    % Including supervisor names and their affiliations is not
                                    % required by the Imperial checklist, but it is considered
                                    % good academic practice and improves clarity.
                                    % The left column lists supervisor names; the right column
                                    % provides their departmental or institutional affiliation.
                                    

  % -------------------------------
  % Submission Date
  % -------------------------------
  \vfill                             % Pushes the date to the bottom of the page.
                                    % Recommended for balanced layout.

  \today                             % Displays the compilation date.
                                     % Optional: may be replaced with the official submission date.
                                     % The Imperial checklist does not require a date on the title
                                     % page, but including one is considered good academic practice.

\end{titlepage}
```

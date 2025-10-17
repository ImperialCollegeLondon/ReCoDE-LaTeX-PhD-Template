PDF=pdflatex
BIB=biber

all: thesis.pdf

thesis.pdf: main.tex chapters/*.tex preamble.tex bibliography.bib
	latexmk -pdf -interaction=nonstopmode -file-line-error main.tex

clean:
	latexmk -C
	rm -f *.bbl *.bcf

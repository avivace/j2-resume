all: pdf base-pdf

pdf:
	python3 j2tex.py -i data.json -t template-redinter.tex -o resume.tex
	xelatex resume.tex

base-pdf:
	python3 j2tex.py -i data.json -t template-nonfancy.tex -o base-resume.tex
	pdflatex base-resume.tex

clean:
	rm *resume.tex
	rm *.log

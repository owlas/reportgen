default: output.pdf

output.pdf: output.tex
	cd build && pdflatex output.tex

output.tex: main.py
	python main.py

clean:
	rm -r build

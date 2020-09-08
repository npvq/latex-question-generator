# IMPORTANT: Rename the sympy folder to "sympy" and add current path to pythonpath in order to use.
from sympy.function import randomProblem

start = r"""\documentclass[10pt,twocolumn]{article}
\usepackage[fontsize=14pt]{scrextend}
\input{./template}
\begin{document}
\section{Derivatives}
\begin{enumerate}
"""

middle = r"""\end{enumerate}
\newpage
\section{Answers}
\begin{enumerate}
"""

end = r"""\end{enumerate}
\end{document}
"""

questions = int(input("Questions >>> "))
difficulty = float(input("Difficulty (0-10) >>> ")) / 10

if difficulty >= 1:
	difficulty = 0.67

file = open("./source/Latex/sample.tex", "w+")
file.truncate()
file.write(start)
qna = {}

for i in range(questions):
	success = False
	while not success:
		try:
			q, a = randomProblem(recur=difficulty)
			qna.update({q: a})
			success = True
		except:
			print("Error")

for j in qna.keys():
	file.write(r"\item \(" + j + r"\)" + "\n")

file.write(middle)

for j in qna.values():
	file.write(r"\item \(" + j + r"\)" + "\n")

file.write(end)

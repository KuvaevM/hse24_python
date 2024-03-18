#!/usr/bin/env python3

def generate_latex_table(data):
    if not data:
        return ""

    num_columns = len(data[0])

    latex_code = "\\begin{tabular}{" + " | ".join(["c"] * num_columns) + "}\n"
    latex_code += "\\hline\n"

    for row in data:
        latex_code += " & ".join(map(str, row)) + " \\\\\n"
        latex_code += "\\hline\n"

    latex_code += "\\end{tabular}"

    return latex_code

def generate_latex_image(image_path):
    latex_code = f"\\includegraphics{{{image_path}}}"
    return latex_code

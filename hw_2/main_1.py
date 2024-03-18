from part_1 import generate_latex_table

table_data = [
    ["Name", "Age", "Gender"],
    ["Alice", 30, "Female"],
    ["Bob", 35, "Male"],
    ["Charlie", 25, "Male"]
]

latex_code = generate_latex_table(table_data)

with open("artifacts/part_1_artifact.txt", "w") as file:
    file.write(latex_code)
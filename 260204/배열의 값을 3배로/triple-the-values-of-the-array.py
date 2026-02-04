matrix = [3, 2, 3], [1, 3, 1], [1, 1, 1]
rows = 3
cols = 3

new_matrix = [
    [element * 3 for element in row]
    for row in matrix
]

for row in new_matrix:
    print(" ".join(str(i) for i in row))
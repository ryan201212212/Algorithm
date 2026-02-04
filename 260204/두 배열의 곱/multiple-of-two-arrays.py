rows = 3
cols = 3

matrix1 = []
while len(matrix1) < rows:
    row = input().split()
    if row:
        matrix1.append(list(map(int, row)))

matrix2 = []
while len(matrix2) < rows:
    row = input().split()
    if row:
        matrix2.append(list(map(int, row)))

for i in range(rows):
    result = []
    for j in range(cols):
        result.append(str(matrix1[i][j] * matrix2[i][j]))
    print(" ".join(result))
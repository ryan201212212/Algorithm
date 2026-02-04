rows = 3
cols = 3
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

for i in range(rows):
    result= []
    for j in range(cols):
        print(str(matrix1[i][j] * matrix2[i][j]))
    print(" ".join(result))

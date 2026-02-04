rows = 3
cols = 3
matrix = [list(map(int, input().split())) for _ in range(rows)]

for i in range(rows): 
    for j in range(cols): 
        print(matrix[i][j] * 3, end=" ") 
    print()

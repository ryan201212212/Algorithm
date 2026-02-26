n = int(input())

for i in range(n) :
    row = list(range(1, n+1))
    
    if i % 2 != 0 :
        row.reverse()
        
    for j in row :
        print(j, end= "")

    print()
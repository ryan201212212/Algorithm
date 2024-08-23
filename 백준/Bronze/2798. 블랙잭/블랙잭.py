N,M = map(int, input().split())
A = list(map(int,input().split()))

max = 0
for i in A :
    for j in A :
        for k in A :
            if i != j and j != k and k != i :
                if i+j+k <= M :
                    if i+j+k > max :
                        max = i+j+k
print (max)

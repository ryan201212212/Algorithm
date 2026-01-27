A, B = map(int, input().split())

while True :
    if A > B :
        break
    print(A, end=" ")
    if A % 2 == 0 :
        A += 3
    elif A % 2 != 0 :
        A *= 2

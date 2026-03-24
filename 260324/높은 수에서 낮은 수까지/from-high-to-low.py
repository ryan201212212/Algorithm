A,B = map(int, input().split())

if A > B :
    i = A
    while i >= B :
        print(i, end=" ")
        i -= 1

elif A < B :
    i = B
    while i >= A :
        print(i, end=" ")
        i -= 1

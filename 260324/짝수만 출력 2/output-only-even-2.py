B, A = map(int, input().split())

if B % 2 != 0 :
    B -= 1

while A <= B :
    print(B, end=" ")
    B -= 2
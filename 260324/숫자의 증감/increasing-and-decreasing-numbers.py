C, N = input().split()
N = int(N)

if C == 'A' :
    i = 1
    while i <= N :
        print(i, end=" ")
        i += 1

elif C == 'D' :
    i = N
    while i <= N :
        print(i, end=" ")
        i -= 1
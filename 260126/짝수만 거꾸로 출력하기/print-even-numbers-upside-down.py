N = int(input())
n = list(map(int, input(). split()))

for i in range(N-1, -1, -1) :
    if n[i] % 2 == 0 :
        print(n[i], end=" ")
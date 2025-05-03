N = int(input())
A = set()

for i in range(N):
    A.add(input())

A = list(A)

A.sort()
A.sort(key = len)

for i in A:
    print(i)
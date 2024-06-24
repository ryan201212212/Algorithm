A = int(input())
B = int(input())
C = int(input())

D = A * B * C
D_s = str(D)

count = [0] * 10
for i in D_s :
    count[int(i)] += 1

for i in range(10):
    print(count[i])

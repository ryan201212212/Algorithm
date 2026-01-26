a, b = map(int, input().split())

answer = [a,b]

for i in range(8) :
    next =(answer[-2] + answer[-1]) % 10
    answer.append(next)
for x in answer:
    print(x, end= ' ')
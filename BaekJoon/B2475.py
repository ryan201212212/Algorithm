n = map(int, input().split())
i = sum(num ** 2 for num in n)
j = i % 10

print(j)
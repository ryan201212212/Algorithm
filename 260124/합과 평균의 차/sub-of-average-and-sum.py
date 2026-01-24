a,b,c = map(int, input().split())

total = a+b+c
average = total / 3
last = total - average

print(total)
print(int(average))
print(int(last))
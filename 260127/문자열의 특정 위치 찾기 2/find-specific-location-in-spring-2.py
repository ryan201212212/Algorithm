N = ["apple", "banana", "grape", "blueberry", "orange"]

n = input()
count = 0
for i in N :
    if i[2] == n or i[3] == n :
        print(i)
        count += 1
print(count)


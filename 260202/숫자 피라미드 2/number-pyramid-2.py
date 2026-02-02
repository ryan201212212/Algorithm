N = int(input())

total = 1
for i in range(1, N+1) :
    sub_total = []
    for j in range(i) :
        sub_total.append(str(total))
        total += 1
    print(" ".join(sub_total))
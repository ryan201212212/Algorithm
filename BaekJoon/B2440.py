n = int(input())
answer = ''
for i in range(0, n+1) :
    answer +=  '*'*(n-i) + '\n'

print(answer)
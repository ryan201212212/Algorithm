n = int(input())
answer = ''
for i in range(1, n+1) :
    answer += (' '*(n-i) + '*'* ((2*i)-1)) + '\n'

print(answer)
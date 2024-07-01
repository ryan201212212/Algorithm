n = int(input())
answer = ''
for i in range(n) :
    answer += ' '* (n-i-1) + '*'*(2*i+1) + '\n'

for i in range(n-2,-1,-1) :
    answer += ' ' * (n-i-1) + '*' * (2*i+1) + '\n'

print (answer)

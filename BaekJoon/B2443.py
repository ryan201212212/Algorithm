
n = int(input())
answer = ''
for i in range(n) :
    answer += ' ' * i + '*' * (2*(n-i)-1) + '\n'

print (answer)


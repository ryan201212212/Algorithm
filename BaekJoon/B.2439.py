n = int(input())
answer = ''
for i in range(1, n+1):
    answer += ' ' * (n - i) + '*'*i +'\n'


print(answer)


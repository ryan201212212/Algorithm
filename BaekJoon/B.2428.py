n = int(input())

for i in range(1, n+1) :
    print ('*' * i)

"""
def solution(n):
    answer = ''
    for i in range(n+1):
        answer += '*' * i + '\n'
    return answer

print(solution(int(n)))
"""

"""
def solution(n) :
    answer = 0
    for i in range(n) :

        answer += i
    return answer

print(solution(6))
"""
"""
def solution(x, n):
    for i in range(n):
        x -= i
    return x

solution(50, 5)

def solution(x, n):
    for i in range(n):
        x -= i
    return x


answer = ''
for i in range(5):
    answer += i

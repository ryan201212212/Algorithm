def solution(n,t) :
    return n * (2**t)


#다른사람 풀이
# << 왼쪽시프트 연산자 : n << m은 n*2의 m승
# >> 오른쪽시프트 연산자 : n >> m은 n/2의 m승
def solution(n, t):
    return n << t


def solution(x1, x2, x3, x4):
    answer = True
    x5 = x1 or x2
    x6 = x3 or x4
    answer = x5 and x6
    return answer

#or 는 교집합 또는 |
#and 는 합집합 또는 &

#다른사람 풀이
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

#다른사람 풀이2
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)
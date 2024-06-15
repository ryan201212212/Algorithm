def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + d * i) * included[i]
    return answer


# 각 항목을 계산하고 결과를 누적하는 변수사용
def solution(a, d, included):
    answer = 0
    num1 = 0
    for i in range(len(included)):
        answer = a + (d * i)
        if included[i]:
            num1 += answer

    return num1
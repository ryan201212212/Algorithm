def solution(n):
    answer = 0
    for i in str(n) :  #문자열로 변경 str()
        answer += int(i)  #다시 정수형 int()로 변경
    return answer
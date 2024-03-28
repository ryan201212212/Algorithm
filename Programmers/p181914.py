def solution(number):
    answer = 0
    for i in number :
        answer += int(i)  #문자열을 정수로 변환 후 합산
    return answer % 9

#루프를 사용하여 숫자의 각 자리를 더하는 과정이 포함되어 있어 세부적인 계산이 가능하다.


#간단한 풀이
def solution(number):
    return int(number) % 9
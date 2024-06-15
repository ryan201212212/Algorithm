
def solution(n):
    answer = 0
    x = int(n ** 0.5) #n의 제곱근을 정수형으로 계산
    if x**2 == n : #n이 제곱근인지 확인
        return (x+1) **2 #제곱수일 경우 (x+1)의 제곱 반환
    else :
        return -1 #제곱수가 아닐 경우 -1 반환
    return answer

#처음 틀린 답  *여기에는 반복문이 필요 없고, 제곱근을 구하는 것이 아니라 제곱을 비교해야 한다.
def solution(n):
    answer = 0
    x = int(n)
    for i in str(n) :
        if x**2 == n :
            answer += (x+1) **2
        else :
            answer += -1
    return answer
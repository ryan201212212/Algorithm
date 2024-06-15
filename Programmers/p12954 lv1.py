def solution(x, n):
    answer = []
    for i in range(n) : #n개 범위에서 반복~
        answer.append(x * (i + 1 )) #반복문에서 생성된 값을 리스트에 추가
    return answer

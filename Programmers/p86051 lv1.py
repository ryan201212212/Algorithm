def solution(numbers):
    answer = [] #빈 리스트로 초기화
    for i in range(10) :  #반복 돌려
        if i not in numbers : #numbers에 숫자 없으면
            answer.append(i)  #answer 리스트에 해당 숫자를 추가한다.
    return sum(answer) #합을 return~~
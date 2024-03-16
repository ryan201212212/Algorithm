def solution(myString):
    answer = []
    for i in myString.split('x') : #x를 기준으로 myString을 split 한다.
        answer.append(len(i)) #순서대로 나열 append
    return answer

#split 함수 기억하기
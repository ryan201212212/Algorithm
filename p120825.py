def solution(my_string, n):
    answer = []
    for i in my_string :
        answer.append(i*n)
    return ''.join(answer) #join 함수는 리스트의 요소들을 하나의 문자열로 함치는 데에 사용된다.



def solution(my_string, num1, num2):
    a = list(my_string) #문자열은 변경할 수 없는 자료형이므로 새로운 문자열을 생성하여 넣어준다.
    a[num1], a[num2] = a[num2], a[num1] #서로 교환
    return ''.join(a)  #리스트를 다시 문자열로 변환하여 반환


#다른 사람의 답변
def solution(my_string, num1, num2):
    answer = ""
    a, b = my_string[num1], my_string[num2]
    for i in range(len(my_string)):
        if i == num1:
            answer += b
        elif i == num2:
            answer += a
        else:
            answer += my_string[i]
    return answer


def solution(my_string):

    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ') #알파벳이면 공백으로 변환
    my_string = my_string.split() #문자열을 공백 기준으로 나눔 (숫자를 개별적으로 처리하기 위함)

    return sum(list(map(int, my_string))) #각 요소 정수형 변환 후 매핑, 숫자들은 정수형으로 저장된 리스트로 만들고 합 계산

#isdigit()
#isalpha()


#틀린 답
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():  # 문자열이 숫자인지 확인
            answer += int(i)  # 숫자면 정수형으로 변환하여 합에 더함
    return answer

#isdigit() 숫자 판별
#isalpha() 알파벳 판별
def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)): #반복 len my_string 안에서
        if my_string[i:] == is_suffix : #my_string 문자열에서 인덱스i부터 끝까지 모든 문자를 포함하는 부분 문자열이 is_suffix와 같다면
            answer = 1 # 1을 answer
    return answer
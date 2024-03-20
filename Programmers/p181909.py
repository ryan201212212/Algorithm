def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])  # [i:]를 쓰는 이유는 부분 문자열을 반환하기 위해서이다.

    answer.sort()  # 순서대로 sort
    return answer
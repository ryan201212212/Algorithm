def solution(my_string):
    answer = [0] * 52  # 52칸 정수 배열을 만들고 0으로 초기화
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    for i in my_string:
        if i in upper:
            index = upper.index(i)
        elif i in lower:
            index = lower.index(i) + 26  # 대문자 뒤로 소문자 인덱스 반영하기 위해 +26 함.
        answer[index] += 1

    return answer
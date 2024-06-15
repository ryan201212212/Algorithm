def solution(s):
    answer = s.lower().count('p') == s.lower().count('y')  # 소문자 변경 후 비교
    return answer


#틀린 답변
def solution(s):
    answer = True
    for i in str(s):
        if 'p' == 'y' in str(s):
            answer += True

    return True


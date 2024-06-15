def solution(q, r, code):
    answer = ''
    for i in range(len(code)) : #들어가자
        if i % q == r: #code를 q로 나누었을 때 나머지  r
            answer += code[i] #문자열에 code[i]추가
    return answer
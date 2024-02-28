def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code) : #code의 배수 위치를 반복
        answer += cipher[i] #해당 위치의 문자를 결과 문자열에 추가
    return answer
def solution(n):
    a = list(str(n)) #문자열로 바꾸고, 자릿수를 리스트로 만든다.
    b = sorted(a, reverse=True) #자릿수 내림차순으로 정렬
    answer = int(''.join(b)) #정렬된 자릿수 리스트를 정수로 변환
    return answer
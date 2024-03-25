def solution(my_string):
    answer = ''
    for i in sorted(my_string.lower()): # 주어진 문자열을 모두 소문자로 변환한 뒤 알파벳 순서대로 정렬
        answer += i #answer에 추가
    return answer
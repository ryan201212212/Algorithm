#간단
def solution(s):
    return ''.join(sorted([char for char in set(s) if s.count(char) == 1]))

#풀어서
def solution(s):
    answer = ''
    # 각 문자의 등장 횟수를 카운트하는 딕셔너리 생성
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # 등장 횟수가 1인 문자들을 answer에 추가
    for char, count in char_count.items():
        if count == 1:
            answer += char

    # 한 번만 등장하는 문자가 없으면 빈 문자열 반환
    if not answer:
        return ''

    # 사전 순으로 정렬하여 반환
    return ''.join(sorted(answer))

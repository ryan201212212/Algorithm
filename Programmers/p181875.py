def solution(strArr):
    answer = []

    for i in range(len(strArr)):  # strArr에서 i 반복
        if i % 2 == 1:
            answer.append(strArr[i].upper())  # 만약 홀수번째 인덱스가 주어지면 대문자로
        else:
            answer.append(strArr[i].lower())  # 아닌 경우에는 소문자로 반환하라

    return answer


#enumerate 사용 답변 (enumerate 함수는 반복 가능한(iterable)객체를 인자로 받아서
# 해당 객체의 요소들을 순회하면서, 각 요소의 인덱스와 값을 순서쌍으로 반환한다.)
def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i,s in enumerate(strArr)]

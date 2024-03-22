def solution(numLog):
    answer = ""
    for i in range(1, len(numLog)):

        diff = numLog[i] - numLog[i - 1]  # 각 단계에서의 수와 이전 단계에서의 수 차이를 계산하여 조작 문자열 생성
        if diff == 1:
            answer += "w"
        elif diff == -1:
            answer += "s"
        elif diff == 10:
            answer += "d"
        elif diff == -10:
            answer += "a"
    return answer

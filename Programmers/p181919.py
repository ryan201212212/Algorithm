def solution(n):
    answer = []

    while n != 1:  # n이 1이 될 때까지 과정 반복한다.
        answer.append(int(n))  # 실수일 수 있는 n을 정수로 변환
        if n % 2 == 0:  # 짝수
            n = n / 2
        else:  # 홀수
            n = 3 * n + 1
    answer.append(1)

    return answer
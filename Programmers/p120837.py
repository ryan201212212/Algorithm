def solution(hp):  # 별도로 장군, 병정, 일개미를 지정할 필요가 없다. 바로 숫자로 진행
    answer = 0

    answer += hp // 5
    hp %= 5

    answer += hp // 3
    hp %= 3

    answer += hp // 1
    hp %= 1

    return answer
def solution(a, b):
    if a > b:  # 만약 a가 b보다 크면 두 값을 교환한다.
        a, b = b, a

    answer = sum(range(a, b + 1))  # a부터 b까지의 합을 구한다.
    return answer
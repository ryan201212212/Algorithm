def solution(a, b):
    answer = 0

    cal1 = int(str(a) + str(b))
    cal2 = 2 * a * b   # 2와 곱하기 때문에 str 없이 2*a*b

    if cal1 > cal2:
        answer = cal1
    elif cal1 < cal2:
        answer = cal2
    else:
        answer = cal1

    return int(answer)
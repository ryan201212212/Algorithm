def solution(a, b):
    answer = 0

    cal1 = int(str(a) + str(b))
    cal2 =  int(str(b) + str(a))

    if cal1 > cal2:
        answer = cal1
    elif cal1 < cal2:
        answer = cal2
    else:
        answer = cal1

    return int(answer)


def solution(a, b):
    answer = 0

    cal1: int(str(a) + str(b))
    cal2: int(str(b) + str(a))

    if cal1 > cal2:
        return cal1
    elif cal1 < cal2:
        return cal2
    else:
        return answer


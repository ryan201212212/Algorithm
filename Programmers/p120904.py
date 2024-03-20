def solution(num, k):
    answer = 0
    n = str(num)
    a = str(k)

    for i in n:
        answer += 1
        if a == i:
            return answer
    return -1
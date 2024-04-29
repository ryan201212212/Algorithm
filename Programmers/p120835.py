def solution(emergency):
    answer = []
    s_emergency = sorted(emergency, reverse=True)

    for i in emergency:
        index = s_emergency.index(i) + 1
        answer.append(index)
    return answer
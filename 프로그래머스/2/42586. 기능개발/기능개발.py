def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)

    for i in range(len(progresses)):
        remaining_work = 100 - progresses[i]
        if remaining_work % speeds[i] == 0 :
            days[i] =  remaining_work // speeds[i]
        else :
            days[i] = remaining_work // speeds[i] + 1

    while days :
        final = days.pop(0)
        count = 1
        while days and days[0] <= final :
            days.pop(0)
            count+= 1
        answer.append(count)

    return answer
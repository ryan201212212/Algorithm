def solution(num_list):
    answer = num_list

    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return num_list

#아래는 나의 틀린 답변
def solution(num_list):
    num_list.sort(reverse=True)
    for i in num_list :
        if int(i-1) > int(i-2) :
            print str(i-1) - str(i-2)
        else :
            print str(i-1) * str(i-2)
    return num_list
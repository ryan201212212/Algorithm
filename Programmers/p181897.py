def solution(n, slicer, num_list):
    answer = []
    if n == 1 :
        answer = num_list[0:slicer[1]+1]
    elif n == 2 :
        answer = num_list[slicer[0]:]
    elif n == 3 :
        answer = num_list[slicer[0]:slicer[1]+1]
    else :
        for i in num_list[slicer[0]:slicer[1]+1:slicer[2]] :
            answer.append(i)
    return answer


#더 효율적인 풀이
def solution(n, slicer, num_list):
    a,b,c=slicer
    if n==1: return num_list[:b+1]
    if n==2: return num_list[a:]
    if n==3: return num_list[a:b+1]
    return num_list[a:b+1:c]
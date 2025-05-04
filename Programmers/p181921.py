def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        if not set(str(i)) - set(['0', '5']): #if i의 각 자리가 '0' 또는 '5'로만 되어 있다면:
            answer.append(i)
    return answer if answer else [-1]
def solution(arr):
    if len(arr) == 1 :  #길이가 1이라면
        return [-1]  #-1 리턴하고
    else : #아니라면
        arr.remove(min(arr)) #가장 작은 arr을 제거해라
    return arr

#처음 틀린 답
def solution(arr):\
    answer = []
    for i in range(len(arr)) :
        answer.sorted(reverse = True)
    return answer(::-1)
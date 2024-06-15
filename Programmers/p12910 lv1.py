#answer 배열이 비어있는지 확인해야한다.
def solution(arr, divisor):
    answer = []
    for i in arr :
        if i % divisor == 0 :
            answer.append(i)
    if len(answer) == 0 : #answer 배열이 비어있으면
        return [-1]  #-1 반환
    else :
        return sorted(answer)
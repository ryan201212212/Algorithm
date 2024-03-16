def solution(array):
    a = max(array)
    b = array.index(a)
    answer = [a,b]
    return answer



#다른사람 풀이 1
def solution(array):
    return [max(array), array.index(max(array))]


#다른사람 풀이 2
def solution(array):
    val = max(array)
    return [val, array.index(val)]
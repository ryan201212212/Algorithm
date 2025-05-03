def solution(arr):
    answer = []
    for i in arr :
        if not answer or answer[-1] != i : #not answer는 answer가 비어있으면 추가, or 다르면 추가
            answer.append(i)
    return answer
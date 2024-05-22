def solution(arr):
    answer = []
    if 2 not in arr : #2가 없으면
        return [-1] #-1 리턴
    else : #2가 있으면
        for i in range(0, len(arr)) : #arr 반복
            if arr[i] == 2: #만약 2가 있으면
                answer.append(i) #arr의 요소를 answer 리스트에 추가하고
    return arr[answer[0]:answer[-1]+1] #첫번째 2가 나타나는 index부터 마지막까지의 부분 배열을 반환
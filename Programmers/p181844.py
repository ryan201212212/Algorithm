def solution(arr, delete_list):
    answer = []
    for i in arr : # arr 반복
        if i not in delete_list : # i가 delete_list에 없다면
            answer.append(i) #순서대로 answer해라
    return answer
def solution(arr, idx):
    answer = 0
    for i in range(idx, len(arr)) : #idx부터 arr까지 안에서 반복하고 len 사용 이유는 리스트 크기 상관없이 유연하게 작업하기 위해서
        if arr[i] == 1 : #만약 arr 속 i가 1이라면
            return i  # i 리턴하고
    return -1  #아니면 -1 리턴해라
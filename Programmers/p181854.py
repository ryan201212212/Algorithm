def solution(arr, n):
    answer = []
    # arr의 길이가 홀수인지 여부에 따라 다르게 처리
    if len(arr) % 2 == 1:
        # 길이가 홀수인 경우, 모든 짝수 인덱스(실제로는 0부터 시작하는 홀수 위치)에 n을 더함
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        # 길이가 짝수인 경우, 모든 홀수 인덱스(실제로는 1부터 시작하는 짝수 위치)에 n을 더함
        for i in range(1, len(arr), 2):
            arr[i] += n
    return arr

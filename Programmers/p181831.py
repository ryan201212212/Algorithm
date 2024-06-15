def solution(arr):
    n = len(arr) #이차원 배열의 크기를 구한 후, 반복문 실행하려고
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] != arr[j][i] :
                return 0
    return 1

#만약 이차원 배열이 n × m 형태로 주어진다면, len(arr) 대신에 len(arr[0])을 사용하여 열의 크기를 가져온다.
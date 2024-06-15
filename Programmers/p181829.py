def solution(board, k):
    answer = 0
    for i in range(len(board)) : #i 지정해주고 len(board)로 2차원 리스트의 행의 개수 반환
        for j in range(len(board[i])): #j 지정해주고
            if i + j <= k :
                answer += board[i][j]
    return answer
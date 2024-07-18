def solution(n, computers):
    def dfs(computer):
        visited[computer] = True
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)

    visited = [False] * n
    answer = 0
    
    for computer in range(n):
        if not visited[computer]:
            dfs(computer)
            answer += 1

    return answer
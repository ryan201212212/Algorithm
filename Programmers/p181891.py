def solution(num_list, n):
    answer = num_list[n:]  # n 번째 원소 이후의 원소들을 먼저 리스트에 추가
    answer += num_list[:n]  # 그 다음, n 번째까지의 원소들을 리스트에 추가

    return answer
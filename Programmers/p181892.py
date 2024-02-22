def solution(num_list, n):
    answer = []
    for i in range(n-1,len(num_list)):
        answer.append(num_list[i])
    return answer

#  나는 옆처럼 잘못 풀었다.  for i in range(1,(num_list),n):
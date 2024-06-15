def solution(num_list, n):
    answer = []
    for i in range(len(num_list)//n) : #num_list는 n의 배수
        answer.append(num_list[n*i : n*(i+1)]) #n*i ~ n(i+1)까지 슬라이싱
    return answer

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer
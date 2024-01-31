def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(i*2)
    return answer

#아래는 다른 풀이 방법
def solution(numbers):
    return [x*2 for x in numbers]
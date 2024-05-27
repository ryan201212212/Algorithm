def solution(n):
    answer = []
    factor = 2 # factor 2 설정
    while n > 1: # n이 1보다 클때 반복
        if n % factor == 0: #n이 factor로 나누어 떨어지면
            if factor not in answer: #factor가 리스트에 없으면 
                answer.append(factor) #추가 
            n //= factor #n을 factor로 나눠
        else: #나누어떨어지지 않으면
            factor += 1 #1증가
    return answer

def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1: #정수 i가 1이 아닌 경우 계속 루프 실행
            if i % 2 == 0: #정수 i가 짝수인 경우
                i /= 2 #2로 나눈다.
            else: #홀수인 경우
                i -= 1 #정수 i에서 -1하고
                i /= 2 #그 결과 값을 2로 나눈다.
            answer += 1 #정수 i를 1로 만들기 위해 필요한 총 연산 획수를 계산한다.
    return answer
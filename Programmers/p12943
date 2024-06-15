def solution(num):
    answer = 0
    while num != 1 :  #수가 1이 아니라면
        if num % 2 == 0 : #짝수인 경우
            num /= 2 #2로 나눈다
        else : #홀수라면
            num = num * 3 + 1 #3을 곱하고 1을 더한다. 
        answer += 1
        if answer == 500 : #만약 작업을 500번 반복 때까지 1아니라면
            return -1 #-1반환
    return answer


# 틀린 포인트 : if num == 500으로 500번 반복했을 때를 검사하는 것은 올바르지 않다. 이 경우는 작업 결과가 500이 되었을 때를 검사하는 것이 아니라, 작업을 500번 반복했을 때를 검사해야 함

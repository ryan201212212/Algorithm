def solution(n):
    i = n ** (1/2) # n ** (1/2)
    if i % 1 == 0 :  #숫자를 1로 나눠서 나머지 0이면 정수
        return 1
    else :
        return 2
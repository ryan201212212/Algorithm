
#순서쌍의 개수 = 약수의 개수
# 어려워서 풀지 못함..
def solution(n):
    answer = []
    for i in range(1,n+1) :
        if n % i == 0 :
            answer.extend([(i, n//i)])
    return len(answer)

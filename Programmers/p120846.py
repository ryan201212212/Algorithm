def solution(n):
    answer = 0
    for i in range(1, n+1) : #1부터 n까지 합성수를 찾는다.
        divisor = 0  #약수의 개수를 나타내기 위해 변수 초기화
        for j in range(1, i+1) : #1부터 i까지 모든 수로 나누어 보면서 약수를 찾기 위해 루프 사용
            if i % j == 0 : # i를 j로 나누어 떨어진다면 (즉, 약수라면)
                divisor += 1 #변수를 증가시킨다.
        if divisor >= 3 : # 약수가 3개 이상인 합성수를 찾는다.
            answer += 1 #변수를 증가시킨다.
    return answer
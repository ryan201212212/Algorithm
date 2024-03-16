def solution(n):
    answer = 0

    if n % 2 == 1:  #n 홀수
        for i in range(1, n + 1): #n 이하의 모든 양의 정수가
            if i % 2 == 1: #홀수라면
                answer += i  #더하라

    else:
        for i in range(1, n + 1): #n 이하의 모든 양의 정수가
            if i % 2 == 0: #짝수라면
                answer += int(i * i) #제곱의 합을  더하라

    return answer


#lambda(익명 함수)를 이용한 고차원 풀이
#lambda 함수가  map 함수와 함께 사용 ( map 함수는 각 요소에 적용하여 결과 생성 )
def solution1(n):
    if n % 2 == 1: # 나머지가 1이라는 결과를 보여주기 위한 코드
        answer = sum(list(map(lambda x : 2*x +1, range(0,(n//2)+1,1)))) #map함수는 lambda 함수를 범위 내의 각 요소에 적용
    else:
        answer = sum(list(map(lambda x : x**2, range(0,n+1,1))))
    return answer
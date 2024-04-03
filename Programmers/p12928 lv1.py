def solution(n):
    answer = 0
    for i in range(1, n+1) :  #1부터 n까지의 수 중에서 n의 약수만을 골라서 더한다.
        if n % i == 0 :
            answer += i
    return answer

#다른사람 풀이 (이렇게 풀려했으나 꼬여버림)
def solution(num):
    return sum([i for i in range(1,num+1) if num%i==0])

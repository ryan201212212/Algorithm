def solution(n):
    answer = ''
    for i in range(n) :
        if i % 2 == 0 :
            answer += '수'
        else :
            answer += '박'
    return answer


#다른 간단한 풀이
def solution(n):
    return ('수박'*n) [:n]  #n이 3일 때, 수박수박수박이 되지만 슬라이싱 사용 > 처음부터 n개의 문자 잘라서 반환


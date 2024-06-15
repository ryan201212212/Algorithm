
#i~j까지 각 숫자를 문자열로 변환하여, 각 숫자에서 k가 등장하는 횟수를 세고 누적하여 반환
def solution(i, j, k):
    answer = 0
    for s in range(i, j + 1):
        answer += str(s).count(str(k))
    return answer


#처음 테스트 3개 중 1개만 통과한 답
def solution(i, j, k):
    answer = 0
    for s in range(i, j+1) :
        if k in range(i, j+1) :
            answer = answer+1
    return answer
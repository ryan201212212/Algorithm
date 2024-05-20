def solution(strArr):
    answer = 0
    countdict = dict() #strArr 원소 저장용 딕셔너리 선언
    for i in strArr : #strArr 순회
        if len(i) in countdict.keys() : #길이가 countdict의 키 값으로 존재하면
            countdict[len(i)] += 1 # +1
        else : #아니라면
            countdict[len(i)] = 1 #1로 할당
    answer = max(countdict.values()) #countdict의 최종값 리턴
    return answer


#딕셔너리 함수 사용할 줄 알아야 한다. 본 코딩은 max나 리스트도 사용할 수 있는 함수였다.

#각 항의 수만 구할 때
def solution(strArr):
    answer = 0
    for i in range(len(strArr)) :
        answer += 1
    return answer
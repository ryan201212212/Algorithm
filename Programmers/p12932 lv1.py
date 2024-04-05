def solution(n):
    answer = []
    for i in str(n) : #str사용해서 문자열 변환하고 돌면서 숫자를 추가
        answer.append(int(i))
    return answer[::-1]

def solution(n):
    answer = []
    for i in str(n) : #str사용해서 문자열 변환하고 돌면서 숫자를 추가
        answer.append(int(i))
    return sorted(answer, reverse=True) #sorted 함수를 사용하면 정확도 15점이라 통과 못함

#sorted 함수는 새로운 리스트를 반환하는 함수이므로 원래 리스트를 변경하지 않는다.
#따라서 원래 리스트를 뒤집고자 할 때에는 sorted 함수를 사용하는 것보다 더 간단한 방법이 있다.

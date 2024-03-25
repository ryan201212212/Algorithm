def solution(myString):
    answer = [i for i in myString.split('x') if i] # 빈 문자열이 아닌 경우에만 추가
    return sorted(answer) # 사전순으로 정렬하여 반환
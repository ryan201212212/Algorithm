def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        j = i[s:s+l] #s번 인덱스에서 시작하여 길이 l짜리 부분 문자열 추출
        if int(j) > k :  # 부분 문자열을 정수로 변환하여 k보다 큰지 확인
            answer.append(int(j))  # k보다 크다면 정수값을 answer에 추가
    return answer

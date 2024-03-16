
#extend method 사용
    answer = []
    for i in arr :
        answer.extend([i]* i)  # i 값을 i번 만큼 answer 배열에 추가
    return answer
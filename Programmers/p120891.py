def solution(order):
    sorder = str(order) #입력을 문자열로 변환
    answer = 0
    for i in sorder :
        if i == '3' or i == '6' or i == '9' :  #''문자열 표시
            answer += 1
    return answer
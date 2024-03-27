def solution(date1, date2):
    answer = 0
    # date1과 date2를 각각의 변수로 분리
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    # 년도를 비교하여 date1이 date2보다 앞서는지 확인
    if year1 < year2 :
        answer = 1
    elif year1 == year2 :
        answer = 0
        if month1 < month2 : # 연도가 같은 경우 월을 비교
            answer = 1
        elif month1 == month2 :
            if day1 < day2:  # 월도 같은 경우 일을 비교
                answer = 1
    return answer
def solution(seoul):
    answer = ''
    for i in range(len(seoul)) : #seoul 배열의 인덱스에 직접 진행
        if seoul[i] == "Kim" : #seoul[i]를 통해 요소의 값을 가져오고, 값이 kim인지 확인
            answer = "김서방은 " + str(i) + "에 있다" #문자열 조합
            break #중단
    return answer

#enumerate함수 사용 답변 킴이 처음 등장하는 위치 찾고, 해당 위치를 문자열에 포함시켜 반환
def solution(seoul):
    answer = ''
    for idx, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 " + str(idx) + "에 있다"
            break
    return answer

#코드 실행은 되었으나 답은 틀린 결과
def solution(seoul):
    answer = ''
    for kim in str(seoul) :
        if kim in seoul :
            answer += 1
    return "김서방은 1에 있다"
#겹치는 부분을 중복하여 세지 않는 방식으로 패턴을 검색해야 한다. 이를 위해서는 문자열을 순회하면서 패턴과 일치하는 부분을 찾아야 한다.
def solution(myString, pat):
    answer = 0
    start = 0
    while True:
        start = myString.find(pat, start) #find() 함수는 문자열에서 특정 패턴을 찾아 해당 위치를 반환하고,
        if start == -1: #찾지 못한 경우 -1을 반환
            break
        answer += 1 #패턴을 찾으면 count를 증가
        start += 1 #다음에 찾을 위치를 현재 위치보다 한 칸 뒤로 옮긴다.
    return answer

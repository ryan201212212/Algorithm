def solution(s):
    arr = s.split(' ')
    answer = []

    for i in arr:  # arr 가보자
        if i == 'Z':  # Z를 만나면
            answer.pop()  # answer 위치의 요소 제거해 'Z'가 나오면 이전에 추가한 값을 취소하는 로직
        else:
            answer.append(int(i))  # 문자열에 있는 숫자 차례대로 추가

    return sum(answer)  # 숫자 더하기
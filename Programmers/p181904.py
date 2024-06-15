
def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)) : #my_string은 문자열이므로 범위를 지정하는데 사용할 수 없으므로 len추가
        if (i+1) % m == c % m : #1부터 시작하는 인덱스를 m으로 나눈 나머지가 몇번째 열에 위치하는지와 m을 c로 나눈 것과 같으면 아래로
            answer += my_string[i] #my_string의 각 문자를 순차적으로, 선택된 열에 해당하는 문자 의미
    return answer

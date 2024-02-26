def solution(numbers, n):
    answer = 0  #0으로 두어야 초기에 0부터 시작한다.

    for i in numbers:  # numbers에 i 반복
        if n < answer:  # 만약 n이 답보다 작으면 그대로 내보내고
            return answer
        else:          # 아닌 경우에는 i를 다 더해라
            answer += i
    return answer



#틀린 내풀이
def solution(numbers, n):
    answer = n         #n으로 두면 첫번째 요소를 더하는 순간 n보다 클 가능성이 있어서 안된다.

    for i in numbers : # numbers에 i 반복
        if sum(i) > n :  # 앞에서부터 하나씩 더한 값이
            return answer
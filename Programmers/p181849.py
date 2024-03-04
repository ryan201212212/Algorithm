def solution(num_str):
    return sum(int(digit) for digit in str(num_str))


#간단한 답변
def solution(num_str):
    answer = 0

    for num in num_str:
        answer += int(num)

    return answer
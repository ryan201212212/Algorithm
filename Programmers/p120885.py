def solution(bin1, bin2):
    a = int(bin1, 2)  # 이진수 문자열을 정수로 변환
    b = int(bin2, 2)

    answer = a + b  # 정수 합
    return bin(answer)[2:]  # bin(result)는 이진수 문자열로 변환하므로 접두사 '0b'붙음 따라서 [2:]로 시작하여 0b 제거


# 오답
def solution(bin1, bin2):
    answer = int(bin1) + int(bin2)
    return str(answer)
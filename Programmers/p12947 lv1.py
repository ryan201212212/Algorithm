def solution(x):
    answer = True
    a = x // 10000  # 만
    b = x // 1000  # 천
    c = x // 100  # 백
    d = x // 10  # 십의자리수 세팅
    e = x % 10  # 일의자리수 세팅
    f = a + b + c + d + e  # 다 더해

    if x % f == 0:  # 나누어 떨어지면
        return answer  # 하샤드 수~
    else:
        return False

#정답코드
    def solution(x):
        a = sum(int(digit) for digit in str(x))  # 각 자릿수의 합 계산

        if x % a == 0:  # x가 자릿수의 합으로 나누어 떨어지는지 검사
            return True
        else:
            return False

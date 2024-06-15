def solution(a, b, c):
    answer = 0

    one = a + b + c
    two = a ** 2 + b ** 2 + c ** 2  # 제곱은 **2
    three = a ** 3 + b ** 3 + c ** 3

    if a != b != c != a:  #a를 한번 더 적어줘야 한다.
        answer = one
    elif a == b == c:
        answer = (one) * (two) * (three)  # 지정해준 것은 ()로 적어준다.
    else:
        answer = (one) * (two)
    return answer
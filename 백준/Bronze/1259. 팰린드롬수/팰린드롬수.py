while True:
    N = input().strip()  # 입력 받기

    if N == '0':  # 입력이 '0'이면 종료
        break

    if N == N[::-1]:  # 숫자 문자열과 그 역순을 비교하여 팰린드롬 여부 판단
        print("yes")
    else:
        print("no")
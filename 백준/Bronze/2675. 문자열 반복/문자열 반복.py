T = int(input()) #케이스의 개수 입력받기

for _ in range(T) :
    R, S = input().split() #문자열 S,R 입력받기
    R = int(R)
    P = ''

    for i in S :
        P += i * R

    print(P)
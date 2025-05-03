H,M = map(int, input().split())

M -= 45

if M < 0 :  #분과 시간의 위치가 바뀌면 틀리게 됨. 분부터 짜야함
    M += 60
    H -= 1

if H < 0 :
    H += 24
    #M += 60 이 줄은 불필요한 코드임

print(H,M)
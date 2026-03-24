A, B = map(int, input().split())
cnt = 0

if A >= 0 :
    for i in range(B) :
        cnt += 1
        print(A, end="")
    
else :
    print(0)
    

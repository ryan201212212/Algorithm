while True :
    a, b, c = map(int, input().split())

    if a== 0 and b == 0 and c == 0 :
        break

    sides = sorted([a,b,c]) #세 변을 오름차순 정렬, 긴 변을 마지막

    if sides[0]**2 + sides[1]**2 == sides[2]**2 : #피타고라스 확인
        print("right")
    else :
        print("wrong")
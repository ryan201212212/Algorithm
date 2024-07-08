def solution(dot):
    x, y = dot[0], dot[1]
    if x>0 and y>0:    #,가 아니라 and 로 연결해줘야 한다.
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4
    else:
        print("원점입니다")   #해줘도 되고 안해줘도 된다.

def solution(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]
#내부리스트 완료 후 외부 리스트(j)에 추가된다.
#바깥[]는 외부 리스트 컴프리헨션이고, 내부[]는 내부 리스트 컴프리헨션이다.
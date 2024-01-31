def solution(slice, n):
    for i in range(1,n):
        if slice*i//n==1:
            return i
def solution(num_list):
    x = '' #짝수
    y = '' #홀수
    for i in num_list :
        if i%2 == 0: #짝수
            x += str(i)
         else :      #홀수
            y += str(i)
    return int(x) + int(y)
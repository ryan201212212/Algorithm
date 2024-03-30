def solution(my_string, s, e):
    reversed_str = list(my_string[s:e+1][::-1]) # 문자열을 리스트로 변환하여 슬라이싱 후 뒤집는다
    my_string = my_string[:s] + ''.join(reversed_str) + my_string[e+1:] ## 뒤집은 부분을 원래 문자열에 대입한다
    return my_string

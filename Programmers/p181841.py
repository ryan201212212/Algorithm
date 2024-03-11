def solution(str_list, ex):
    answer = ''
    for i in str_list :  #range 없이 작성
        if ex not in i :  #ex가 i에 없다면
            answer += i   #i 출력해라
    return answer
ㅔ


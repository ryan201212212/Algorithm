def solution(code):
    answer = ''
    mode = 0 #정수

    for idx, i in enumerate(code) :
        if mode == 0 :
            if i != '1' :
                if idx % 2 == 0 :
                    answer += i
            else:
                mode = 1
        else :
            if i != '1' :
                if idx % 2 != 0 :
                    answer += i
            else :
                mode = 0
    return answer
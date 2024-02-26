def solution(n, control):
    answer = n

    for k in control:
        if k == "w":
            answer += 1
        elif k == "s":
            answer -= 1
        elif k == "d":
            answer += 10
        elif k == "a":
            answer -= 10

    return answer



#틀린 풀이 ex)

elif k in control :
"s" -= -1
elif k in contrl :
"d" += 10
else :
"a" -= 10
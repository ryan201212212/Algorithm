n = str(input())
answer = 0
in_word = False

for i in n :
    if i in ' ' :
        if in_word :
            in_word = False

    else :
        if not in_word :
            answer += 1
            in_word = True

print(answer)

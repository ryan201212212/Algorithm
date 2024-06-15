def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)) :
        if i not in indices :  #만약 i가 indices에 없다면
            answer += my_string[i] #추가하라~
    return answer
def solution(my_string, is_prefix):
    answer = 0
    for i in range(len(my_string)):
        if my_string[:i] == is_prefix :
            answer = 1
    return answer


#다른사람 풀이
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))
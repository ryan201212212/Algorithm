def solution(my_string, target):
    answer = 0
    for i in range(len(my_string)) :
        if target in my_string :
            answer = 1
        else :
            answer = 0
    return answer


#re함수를 사용한 풀이
import re
def solution(my_string, target):
    if re.search(re.escape(target), my_string):
        return 1
    else:
        return 0
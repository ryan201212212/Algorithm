def solution(my_string, index_list):
    answer = ''
    for i in index_list : #index_list의 각 원소에 대해 반복
        answer += my_string[i] #해당 인덱스의 문자를 answer에 추가
    return answer




#다른 풀이
def solution(my_string, index_list):
    # 리스트 컴프리헨션을 사용하여 index_list의 각 인덱스에 해당하는 my_string의 문자들을 추출
    # 그리고 join() 메서드를 사용하여 이 문자들을 하나의 문자열로 합침
    return ''.join([my_string[i] for i in index_list])
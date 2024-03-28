def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string)) #''.join은 각 요소들을 빈 문자열로 구분하여 하나의 문자열로 결합
    return answer

#dict.fromkeys() 메서드는 딕셔너리를 생성하는 파이썬의 내장 메서드 중 하나입니다.
#이 메서드는 주어진 키(key)의 리스트나 이터러블(iterable)로부터 새로운 딕셔너리를 생성
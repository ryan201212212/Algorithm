def solution(array):
    answer = ""
    for i in array:  # array의 인덱스 반복문
        answer += str(i)  # 인덱스 문자열 변환

    return answer.count("7")  # count()함수를 이용하여 7의 개수를 구해 return

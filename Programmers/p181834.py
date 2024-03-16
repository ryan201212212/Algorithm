def solution(myString):
    answer = ''
    for i in myString :
        if i < 'l' :  #만약 반복문 i 가 l보다 작다면0
            answer += 'l' # l로 답변하고
        else :      #아닌 경우라면
            answer += i  #그대로 답변해라
    return answer
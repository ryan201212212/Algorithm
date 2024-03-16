def solution(rsp):
    answer = ''

    for i in rsp:
        if i == '0' :
            answer += '5'
        elif i == '2' :
            answer += '0'
        elif i == '5' :
            answer += '2'
    return answer


#다른 사람 딕셔너리를 만들어서 get()을 사용 후 value 값을 찾은 경우
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'} #딕셔너리
    return ''.join(d[i] for i in rsp) #''join을 이용하여 하나로 합쳤고, 간단히 dict[k]룰 사용하여 value 가져옴.
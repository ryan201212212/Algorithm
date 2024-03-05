def solution(my_strings, parts):
    answer = [] #빈 리스트 answer 생성
    for i in range(len(my_strings)) : #for 루프를 사용하여 my_strings 선회
        s,e = parts[i] #parts[i] = [s,e] 형태의 명령어
        a = my_strings[i][s:e+1] #my_strings[i] 문자열 s~e까지 부분 문자열 추출 및 추출한 부분 문자열을 a에 저장
        answer.append(a) #answer 리스트에 추가
    return ''.join(answer)



#answer를 ''로 두면 'str' object has no attribute 'append'라는 오류가 뜬다.
#이유는  answer가 문자열인데, append 메서드는 리스트에만 사용할 수 있기 때문이다.
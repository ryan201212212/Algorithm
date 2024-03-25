def solution(age):
    age = str(age)
    age = age.replace("0", "a")
    age = age.replace("1", "b")
    age = age.replace("2", "c")
    age = age.replace("3", "d")
    age = age.replace("4", "e")
    age = age.replace("5", "f")
    age = age.replace("6", "g")
    age = age.replace("7", "h")
    age = age.replace("8", "i")
    age = age.replace("9", "j")
    return age


#다른사람 답 (리스트로 만들어서 join으로 문자열 만드는 방식)
def solution(age):
	return ''.join([chr(int(i)+97) for i in str(age)])

#다른 사람 답2 (translate: 매핑 테이블을 기반으로 문자열 변환/maketrans:문자열 매핑 테이블 만듦)
def solution(age):
    return str(age).translate(str.maketrans('0123456789', 'abcdefghij'))

#다른사람 답3
def solution(age):
    answer = ''
    for i in str(age):
        answer += chr(int(i) + 97)
    return answer
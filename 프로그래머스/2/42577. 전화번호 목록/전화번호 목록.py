def solution(phone_book):
    answer = True #변수 초기화
    phone_book.sort() #정렬
    
    for i in range(len(phone_book) - 1) : #인접한 번호들만 비교 
        if phone_book[i + 1].startswith(phone_book[i]): #다음번의 접두어인지 확인
            answer = False
            break
    
    return answer
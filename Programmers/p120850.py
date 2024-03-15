def solution(my_string):
    answer = []
    for i in my_string :
        try :
            answer.append(int(i))  #i가 int로 형변환이 가능하면 answer에 추가하고
        except:
            continue  #불가능하면 continue한다.
    answer.sort()   #정렬한다.
    return answer
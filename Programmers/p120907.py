def solution(quiz):
    answer = []
    for i in quiz :
        j = i.split(' ')  # 수식을 공백을 기준으로 분리하여 X, 연산자, Y, 등호, Z로 분리
        X = int(j[0])
        Op = j[1]  #연산자
        Y = int(j[2])
        Z = int(j[4])
        if Op == '+' and X + Y == Z :
            answer.append("O")
        elif Op == '-' and X - Y == Z :
            answer.append("O")
        else :
            answer.append("X")
    return answer
def solution(binomial):
    a, op, b = binomial.split()
    if op == '+': return int(a) + int(b)
    if op == '-': return int(a) - int(b)
    if op == '*': return int(a) * int(b)
    if op == '/': return int(a) / int(b)


    #다른 사람 풀이
    def solution(binomial):
        return eval(binomial)  #매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수
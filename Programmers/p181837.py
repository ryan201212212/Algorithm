#수정 답
def solution(order):
    answer = 0

    americano_price = 4500
    cafelatte_price = 5000

    for i in order:
        if i in ["americano", "iceamericano", "americanoice", "hotamericano", "americanohot", "anything"]:
            answer += americano_price
        elif i in ["cafelatte", "icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot"]:
            answer += cafelatte_price
    return answer

#나의 오답
def solution(order):
    answer = 0

    americano_price = 4500
    cafelatte_price = 5000

    for i in order :
        if "americano" or "iceamericano" or "americanoice" or "hotamericano" or "americanohot" or "anything" in i :
            answer += americano_price
        elif "cafelatte" or "icecafelatte" or "cafelatteice" or "hotcafelatte" or "cafelattehot" in i :
            answer += cafelatte_price
    return answer
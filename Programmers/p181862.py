def solution(myStr):
    answer = []
    for i in ["a", "b", "c"] :  # a,b,c 있으면
        myStr = myStr.replace(i, " ") #myStr의 i를 공백으로 두고
    answer = myStr.split() #나눈다
    if not answer : #아니라면
        answer = ["EMPTY"] #공백으로 둔다.
    return answer


#나의 오답
def solution(myStr):
    answer = []
    for i in myStr :
        if "[abc]" in i :
            i.split("[abc]", myStr())
        else :
            return ["EMPTY"]
    return i
#rsplit은 문자열을 오른쪽부터 분리하는 함수
def solution(myString, pat):
    return myString.rsplit(pat,1)[0] + pat
#pat 기준 오른쪽으로 1번 분리하고, 분리된 부분의 첫부분 반환 + pat를 추가하여 반환
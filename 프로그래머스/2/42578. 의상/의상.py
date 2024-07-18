def solution(clothes):
    from collections import defaultdict
    
    clothes_dict = defaultdict(int) #의상의 종류별 개수 저장할 딕셔너리 
    
    for item, category in clothes : #의상의 종류별로 개수를 세기
        clothes_dict[category] += 1
        
    answer = 0 #초기값 0
    
    for i in clothes_dict.values() :
        answer *= (i + 1) #의상을 선택하지 않은 경우도 포함
        answer += i #선택한 경우
    
    return answer
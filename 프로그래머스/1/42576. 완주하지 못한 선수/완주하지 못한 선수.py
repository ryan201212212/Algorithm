from collections import Counter

def solution(participant, completion):

    all = Counter(participant)
    comp = Counter(completion)
    result = all - comp
    
    return list(result)[0]
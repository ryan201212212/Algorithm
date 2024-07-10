from collections import Counter

def solution(participant, completion):

    c_participant = Counter(participant)
    c_completion = Counter(completion)
    result = c_participant - c_completion
    
    return list(result.keys())[0]
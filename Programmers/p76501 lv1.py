def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)) :  # absolutes의 길이만큼 반복
        if signs[i] : # 만약 signs[i]가 True이면 해당 숫자를 더한다~
            answer += absolutes[i]
        else : # signs[i]가 False이면 해당 숫자의 부호를 바꾼 뒤 더한다~
            answer -= absolutes[i]
    return answer

#다른사람 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
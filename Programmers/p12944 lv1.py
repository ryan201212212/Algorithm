def solution(arr):
    answer = 0
    for i in arr :
        answer += i #요소를 누적한다.
    answer /= len(arr) #answer에 저장된 값을 배열의 길이로 나눈 후 다시 answer에 할당한다.
    return answer

#다른사람 풀이
def solution(arr):
    return sum(arr) / len(arr) #배열 arr의 합을 구해 배열 arr의 길이만큼 나눠 리턴한다.
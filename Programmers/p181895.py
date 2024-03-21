def solution(arr, intervals):
    a1, b1 = intervals[0] #intervals 리스트에서 첫번째 튜플의 시작과 끝 인덱스를 a1과 b1에 할당
    a2, b2 = intervals[1] #두번째 튜플의 시작과 끝 인덱스를 a2와 b2에 할당
    return arr[a1:b1+1] + arr[a2:b2+1] #arr리스트에서 각 구간에 해당하는 부분을 슬라이싱하여 추출
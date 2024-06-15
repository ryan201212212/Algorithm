def solution(array, n):
    array.sort() #정렬
    answer = array[0] #초기값(첫번째 요소)을 array[0]으로 설정함.
    x = abs(n - array[0]) #매개변수n과 첫번째 요소 값 차의 절대값을 x로 설정
    for i in array : # array 반복
        if x > abs(n-i) : #만약 i가 n에 가까운 값이라면(x보다 작다면)
            x = abs(n-i) #x를 업데이트하고
            answer = i #i로 할당
    return answer

#abs는 절대값
#어려웠다
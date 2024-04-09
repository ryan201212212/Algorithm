
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        row = []
        for j in range(len(arr1[i])) :
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer



#arr1과 arr2를 다시 정의할 필요가 없고, 문자열로 더한 값이 아닌 행렬로 더해야 한다.
def solution(arr1, arr2):
    answer = [[]]
    arr1 = str[['a11', 'a12'],['b11', 'b12']]
    arr2 = str[['c11', 'c12'],['d11', 'd12']]
    w = 'a11+b11'
    x = 'a12+b12'
    y = 'c11+d11'
    z = 'c12+d12'
    return [w,x],[y,z]
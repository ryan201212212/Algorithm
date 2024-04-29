def solution(arr, queries):
    for i,j in queries :
        for s in range(i,j+1) :
            arr[s]+=1
    return arr
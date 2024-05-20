def solution(arr, queries):
    for i in queries :
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]  # python의 특징인 병렬 할당을 활용

    return arr
def solution(arr1, arr2):
    answer = 0

    for i in range(len(arr1)):
        a = sum(arr1)

    for j in range(len(arr2)):
        b = sum(arr2)

        if (len(arr1) < len(arr2)):
            answer = -1
        elif (len(arr1) > len(arr2)):
            answer = 1
        else:
            if a > b:
                answer = 1
            elif a == b:
                answer = 0
            else:
                answer = -1
    return answer
    return answer


#다른사람 풀이
def solution(arr1, arr2):
    answer = 0
    for i in range(len(arr1)):
        hap1 = sum(arr1)

    for j in range(len(arr2)):
        hap2 = sum(arr2)

        if (len(arr1) < len(arr2)):
            answer = -1
        elif (len(arr1) > len(arr2)):
            answer = 1
        elif (len(arr1) == len(arr2) and hap1 > hap2):
            answer = 1
        elif (len(arr1) == len(arr2) and hap1 == hap2):
            answer = 0
        elif (len(arr1) == len(arr2) and hap1 < hap2):
            answer = -1

    return answer
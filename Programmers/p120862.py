def solution(numbers):
    numbers.sort()  #정렬 오름차순 (만약 내림차순이면 sort(reverse = True))
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1]) #가장 큰 두수를 선택하여 곱한다.

#가장 큰 두수의 곱, 가장 작은 두 수의 곱 중 더 큰 값을 선택하여 반환
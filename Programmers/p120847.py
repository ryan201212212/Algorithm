def solution(numbers):
    numbers.sort() #sort정렬해서 순서대로 만들고
    return numbers[-2] * numbers[-1]  #numbers 중 두 개를 곱해섯 만들 수 있는 최댓값은 끝의 두자리


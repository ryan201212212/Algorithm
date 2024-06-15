"""
초기화, 길이 지정해준다.
i가 1보다 작을 때까지 2로 나누어준다.
a변수에 저장한다.
기존 리스트에 + 2제곱으로 맞추기 위해 0을 추가한다.
"""

def solution(arr):
    a = 0
    i = len(arr)
    while i > 1:
        i = i / 2
        a += 1
    return arr + [0]*(2**a - len(arr))
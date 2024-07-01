N = int(input())
numbers = list(map(int, input().split())) #map 함수를 사용하여 입력받은 값을 정수 리스트로 변환

min_di = min(numbers)
max_di = max(numbers)

N = min_di * max_di

print(N)

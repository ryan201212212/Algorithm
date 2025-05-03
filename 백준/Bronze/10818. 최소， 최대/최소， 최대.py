N = int(input()) #첫째줄 케이스 정수의 개수 입력받기
numbers = list(map(int,input().split())) #둘째줄 N개의 정수 공백으로 입력받고, 정수 리스트로 변환

min_num = min(numbers)
max_num = max(numbers)

print(min_num, max_num)
N = int(input()) #첫째줄 케이스 정수의 개수 입력받기
member_lst = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in member_lst:
    print(i[0], i[1])
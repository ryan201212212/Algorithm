n = int(input())   #첫째줄에 입력 개수를 정수로 입력

answer = []  #각 줄의 합을 저장할 리스트 초기화
for i in range(n) :
    A,B = map(int, input().split())
    answer.append(A+B) #A와B합을 리스트에 추가

for sum in answer : #리스트에 저장된 각 합을 순차적으로 출력
    print(sum)
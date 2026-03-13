a = int(input())
answer = 0

if a % 2 == 0 :
    answer=int((a/2))
if answer % 2 != 0 :
    answer = int(((answer+1)/2))

print(answer)

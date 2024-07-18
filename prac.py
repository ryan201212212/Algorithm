
import random

target = random.randint(1, 10)

while True :
    guess = int(input("숫자를 입력하세요 :"))
    if guess == target :
        print("정답입니다")
        break
    elif guess < target :
        print("target은 좀 더 큰 숫자입니다")
    elif guess > target :
        print("target은 좀 더 작은 숫자입니다")
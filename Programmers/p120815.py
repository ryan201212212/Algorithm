def solution(n):
    answer = 1  # n이 6이면 while문 들어갈 수 없으므로 그대로 return 된다.

    while (answer * 6) % n != 0:  # 피자의 개수와 피자조각 곱해주고 사람인원으로 나눌 때 나머지 0이면
        answer += 1  # 모두가 먹은 것~~

    return answer

#for문 : 원하는 횟수만큼 반복문 실행
#while문 : 몇 번 수행해야 할 지 모르는 상황에서 특정 조건이 만족될 때까지 수행하는 경우

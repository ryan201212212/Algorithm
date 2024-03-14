def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)
#가로 // n 하여 몫 반환 * 세로 // n하여 몫 반환 * 높이 // n하여 몫 반환
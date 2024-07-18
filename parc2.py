person_a_nums = [70, 85, 90, 60]
person_b_nums = [30, 75, 30, 90]
person_c_nums = [20, 55, 70, 60]

total_score = 0
for i in person_a_nums :
    total_score += i
average_score = total_score / 4

print(f"person_a의 평균점수는 {average_score}")
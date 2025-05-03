person_a_numbers = [70, 85, 90, 60]
person_b_numbers = [30, 75, 30, 90]
person_c_numbers = [20, 55, 70, 60]

def calc_avg(name, numbers) :
    total_score = 0
    for i in numbers :
        total_score += i
    average_score = total_score / 4

    print(f"{name}의 평균점수는 {average_score}")

calc_avg("person_a", person_a_numbers)
calc_avg("person_b", person_a_numbers)
calc_avg("person_c", person_a_numbers)
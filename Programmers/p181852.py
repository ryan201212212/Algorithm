def solution(num_list):
    num_list.sort()
    return num_list[5:] if len(num_list) > 5 else []

example_list = [12, 4, 15, 46, 38, 1, 14, 56, 32, 10]
result = solution(example_list)
print(result)  # [10, 12, 15, 17, 19, 20]
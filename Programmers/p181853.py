def solution(num_list):
    num_list.sort()
    return num_list[:5]


if __name__ == '__main__':
    print(solution([12, 4, 15, 46, 38, 1, 14]))

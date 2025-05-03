def solution(nums):
    count = len(set(nums))
    max_nums = len(nums) // 2

    return min(count, max_nums)
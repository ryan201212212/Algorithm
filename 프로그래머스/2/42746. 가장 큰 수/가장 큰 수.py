def solution(numbers):
    numbers = list(map(str, numbers))
    
    def compare(x, y):
        if x+y > y+x :
            return -1
        elif x+y < y+x :
            return 1
        else:
            return 0
    
    numbers.sort(key=lambda x: x*4, reverse=True)
    
    if numbers[0] == '0':
        return '0'
    
    answer = ''.join(numbers)
    return answer
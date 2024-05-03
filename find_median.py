# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 05/02/2024
# Description: Program that returns the statistical median of a list of numbers.

def find_median(num):
    '''Functions that finds the statistical median from a list'''
    if not num:
        return None
    
    sorted_num = sorted(num)
    print(sorted_num)
    
    numbers = len(sorted_num)
    print(numbers)
    middle_index = numbers // 2
    print(middle_index)

    if numbers % 2 == 1:
        return sorted_num[middle_index]
    else:
        return (sorted_num[middle_index - 1] + sorted_num[middle_index] / 2 )

values = [1, 2, 3, 4, 5, 6]
result = find_median(values)

print(result)

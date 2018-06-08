

def largest_cont_sum(data_list):
    if not isinstance(data_list, list):
        raise TypeError('The data_list need to be a list.')
    if len(data_list) < 1:
        return 0

    largest_sum = 0
    sz = len(data_list)
    for i in range(sz):
        for j in range(i, sz):
            current_sum = sum(data_list[i:j])
            if largest_sum < current_sum:
                largest_sum = current_sum

    return largest_sum


print( largest_cont_sum([1,-3, 1, 2,-1,3,4,10,10,-10,-1]) )  #29

import sys

def largest_cont_sum_better(data_list):
    if not isinstance(data_list, list):
        raise TypeError('The data_list need to be a list.')
    if len(data_list) < 1:
        return 0

    current_sum = data_list[0]
    max_sum = data_list[0]

    for num in data_list[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


print( largest_cont_sum_better([-1,1]) )   #1
print( largest_cont_sum_better([1,2,-1,3,4,-1]) )   #9
print( largest_cont_sum_better([1,-3, 1, 2,-1,3,4,10,10,-10,-1]) )  #29
print( largest_cont_sum_better([-2,-1]) )  #-1

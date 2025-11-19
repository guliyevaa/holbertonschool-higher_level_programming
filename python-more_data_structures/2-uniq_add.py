#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = []
    for num in my_list:
        if num not in unique_values:
            unique_values.append(num)
    return sum(unique_values)

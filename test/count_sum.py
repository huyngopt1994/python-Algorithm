def count_sum(array, expected_sum):
    count = 0
    my_dict = {}
    for item in array:
        if my_dict.get(expected_sum - item):
            count += 1
            del my_dict[expected_sum - item]
            continue
        else:
            my_dict[item] = 'Yes'
    print(count)


count_sum([1, 5, 3, 5, 2, 1, 4, 3], 6)

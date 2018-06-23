# Yep we will do in 2 case

def calculate_min_max(arr):
    my_dict = {'max': None,
               'min': None,}
    # O(n)

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        sum = 0

        for item in new_arr:
            sum += item
        if my_dict['max']:
            if  sum > my_dict['max']:
                my_dict['max'] = sum
        else:
            my_dict['max'] = sum

        if my_dict['min']:
            if sum < my_dict['min']:
                my_dict['min'] = sum
        else:
            my_dict['min'] = sum

    print('%s %s' % (my_dict['min'], my_dict['max']))

my_dict = {'max': None,
           'min': None,
           }

def calculate_min_max_recursive(k,arr):
    if k <0:
        print('%s %s' % (my_dict['min'], my_dict['max']))
        return 0
    sum = 0
    new_arr = arr[:k] + arr[k+1:]
    for i in new_arr:
        sum += i
    if my_dict['max']:
        if sum > my_dict['max']:
            my_dict['max'] = sum
    else:
        my_dict['max'] = sum

    if my_dict['min']:
        if sum < my_dict['min']:
            my_dict['min'] = sum
    else:
        my_dict['min'] = sum

    return calculate_min_max_recursive(k-1, arr)
calculate_min_max_recursive(len([1,2,3,4,5])-1, [1,2,3,4,5])
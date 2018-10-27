# Using two pointers  http://codeforces.com/problemset/problem/224/B
n_number, k_number = list(map(int, input().split()))
numbers = list(map(int, input().split()))


def get_l_array():
    count = 0
    collected_unique_numbers = {}
    for i in range(n_number):
        if numbers[i] in collected_unique_numbers:
            collected_unique_numbers[numbers[i]] += 1
        else:
            count += 1
            collected_unique_numbers[numbers[i]] = 1
            if count == k_number:
                return collected_unique_numbers, numbers[:i + 1]
    return collected_unique_numbers, [-1, -1]


def get_the_smallest_array(unique_numbers, first_array):
    for i in range(len(first_array)):
        unique_numbers[first_array[i]] -= 1
        if unique_numbers[first_array[i]] == 0:
            return [str(i + 1), str(len(first_array))]


unique_numbers, first_array = get_l_array()
if first_array == [-1, -1]:
    print('-1 -1')
else:
    final_result = get_the_smallest_array(unique_numbers, first_array)
    print(' '.join(final_result))

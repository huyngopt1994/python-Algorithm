# https://www.hackerrank.com/challenges/migratory-birds/problem
from collections import defaultdict


def get_the_result(my_input):
    max = 0
    dict_type = {}
    dict_freq = defaultdict(set)
    # O(n) time
    for bird in my_input:
        if dict_type.get(bird):
            dict_type[bird] += 1
        else:
            dict_type[bird] = 1
        # check max
        if max <= dict_type[bird]:
            max = dict_type[bird]
            dict_freq[max].add(bird)

        # update current

    # nlog(n)
    return sorted(dict_freq[max])[0]


numbers = int(input())
custom_inputs = list(map(int, input().split()))
result = get_the_result(custom_inputs)
print(result)

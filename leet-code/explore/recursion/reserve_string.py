import math


def simple_work_with_iterating_with_o_1_complexity(my_input):
    l = len(my_input)
    for i in range(math.floor(l // 2)):
        my_input[i], my_input[l - 1 - i] = my_input[l - 1 - i], my_input[i]

    print(my_input)


def simple_work_with_recursion_with_O_n_complexity(my_input, expected_result):
    if len(my_input) == 1:
        return my_input[0]
    result = simple_work_with_recursion_with_O_n_complexity(my_input[1:], expected_result)
    if result:
        expected_result.append(result)
    expected_result.append(my_input[0])


def simpe_work_with_recurison_with_o_1_complextity(str):
    def helper(start, end):
        if start >= end:
            return
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
        helper(start, end)

    helper(0, len(str) - 1)


result = ["o", "e", "l", "l", "h"]
simpe_work_with_recurison_with_o_1_complextity(result)

print(result)

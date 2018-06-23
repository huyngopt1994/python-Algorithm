"https://www.hackerrank.com/challenges/validating-postalcode/problem"
import re

group_pattern1 = '^[4-6][0-9]{15}$'
group_pattern2 = '^[4-6][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'

my_input = int(input())


def verify(your_input):
    if not (re.match(group_pattern1, your_input) or re.match(group_pattern2, your_input)):
        return False
    # check if we have continuous
    count = 1
    pre = ''
    for i in your_input:
        if i == '-':
            continue
        else:
            if i == pre:
                count += 1
            else:
                pre = i
                count = 1
        if count > 3:
            return False
    return True


for _ in range(my_input):
    one_line = input()
    if verify(one_line):
        print('Valid')
    else:
        print('Invalid')


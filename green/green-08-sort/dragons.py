import sys

sys.setrecursionlimit(9900)


class Dragon(object):
    def __init__(self, req, inc):
        self.req = req
        self.inc = inc


def verify_dragons(higher, current):
    if len(higher) == 0:
        return True
    position = -1
    for i in range(len(higher)):

        if (current) > higher[i].req:
            current += higher[i].inc
            # move item from higher => lower

            position = i
            break

    if position >= 0:
        del higher[position]
        return verify_dragons(higher, current)
    else:
        return False


def bubble_sort_desending(my_list):
    """key is inc"""
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # try to swap if my_list[i] = my_list[j]
            if my_list[i].inc < my_list[j].inc:  # if lower swap
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
            elif my_list[i].inc == my_list[j].inc:
                # sort following req
                if my_list[i].req > my_list[j].req:
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp

    return my_list


lower = []
higher = []
current_s, numbers = map(int, input().split())

for _ in range(numbers):
    current_r, increase = list(map(int, input().split()))
    if current_r >= current_s:
        higher.append(Dragon(current_r, increase))
    else:
        lower.append(Dragon(current_r, increase))

# higher ( descending with req)
higher = bubble_sort_desending(higher)

# first try to fight lower firstly
for item in lower:
    current_s += item.inc

if verify_dragons(higher, current_s):
    print('YES')
else:
    print('NO')

# http://codeforces.com/problemset/problem/691/A?fbclid=IwAR0lm5qeAQE4z59GCXOl7qTYgiAW0eFQyYnXSBHDh9quxdfdzIU4sa3tCB4
number_buttons = int(input())
buttons = list(map(int, input().strip().split()))


def check_is_fastened(my_number_buttons, my_buttons):
    if my_number_buttons == 1:
        if my_buttons[0] == 0:
            return 'NO'
        else:
            return 'YES'
    num_of_o = 0
    for button in my_buttons:
        if button == 0:
            num_of_o += 1
        if num_of_o > 1:
            return 'NO'
    if num_of_o == 1:
        return 'YES'
    else:
        return 'NO'


print(check_is_fastened(number_buttons, buttons))

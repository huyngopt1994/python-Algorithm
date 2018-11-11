# https://www.spoj.com/problems/MMASS/
# solution : check from left to right:
"""
get C/H/O => add stack
get "(" => add Stack
get ")" => start get all element to "(" => if got C/H/0 => sum
if got => "number" => get the next * print this number => sum
=> sum all => and push to this stack again
get "number" => pop the prefix => mul => and push to stack again

after all => sum this stack
"""
"""example
CH(CO2H)3
12 1 135
"""
formula = list(input().strip())

stack = []
refers = {'C': 12, 'H': 1, 'O': 16}

for c in formula:
    if c == ')':
        # try to solve  the rest of thing until reach '('
        value = stack.pop()
        my_sum = 0
        while value != '(':
            if isinstance(value, int):
                # the value before
                my_sum += value
            elif value.isdigit():
                # get index:
                pre_value = stack.pop()
                if isinstance(pre_value, int):
                    my_sum += (pre_value * int(value))
                elif pre_value.isalpha():
                    my_sum += (int(value) * refers[pre_value])
                else:
                    break  # '('
            else:
                my_sum += refers[value]
            value = stack.pop()
        stack.append(my_sum)
    elif c in ['C', 'H', 'O', '2', '3', '4', '5', '6', '7', '8', '9', '(']:
        stack.append(c)

result = 0
while stack:
    item = stack.pop()
    if isinstance(item, int):
        result += item
    elif item.isalpha():
        result += refers[item]
    else:
        pre_value = stack.pop()
        if isinstance(pre_value, int):
            result += (pre_value * int(item))
        elif pre_value.isalpha():
            result += (int(item) * refers[pre_value])

if result > 10000:
    result = 10000
print(result)

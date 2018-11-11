# http://www.spoj.com/problems/ONP/
number_of_expression = int(input())

piorties = ['+', '-', '*', '/', '^']


def convert_onp(custom_input):
    output = ''
    stack = []
    for c in custom_input:

        if c == ' ':
            continue
        if c.isalpha():
            output += c
            continue
        if c == '(':
            stack.append(c)
        if c == ')':
            item = stack.pop()
            while item != '(':
                output += item
                item = stack.pop()
            continue
        if c in piorties:
            if stack[-1] in piorties and piorties.index(stack[-1]) > piorties.index(c):
                output += stack.pop()
                stack.append(c)
            else:
                stack.append(c)
    return output


for _ in range(number_of_expression):
    print(convert_onp(input()))

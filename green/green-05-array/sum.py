import functools
number = input()
array_number = map(int, input().split())

sum = functools.reduce(lambda a, b: a+b, array_number)
print(sum)


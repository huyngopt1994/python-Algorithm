# http://codeforces.com/contest/451/problem/B
# get input firstly:
number = int(input())
numbers = list(map(int, input().split()))
j = 1

my_sorted = sorted(numbers)


def test(number, numbers):
    if number == 1:
        print('yes')
        print('1 1')
        return
    if numbers == my_sorted:
        print('yes')
        print('1 1')
        return
    l = 0
    for i in range(0, number):
        if my_sorted[i] != numbers[i]:
            l = i
            break
    r = number - 1
    for j in range(number - 1, 0, -1):
        if my_sorted[j] != numbers[j]:
            r = j
            break
    if numbers[l:r+1][::-1] == my_sorted[l:r+1]:
        print('yes')
        print('{}  {}'.format(l + 1, r + 1))
    else:
        print('no')


test(number, numbers)

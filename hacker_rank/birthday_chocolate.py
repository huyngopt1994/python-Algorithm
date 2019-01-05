# https://www.hackerrank.com/challenges/the-birthday-bar/problem
number_of_chocolate = int(input())
squares_of_cho = list(map(int, input().split()))
d, m = list(map(int, input().split()))
# get the number of bar have length = m , sum = d
count = 0
if m <= number_of_chocolate:
    i = 0
    while (i + m) <= number_of_chocolate:
        if sum(squares_of_cho[i:i + m]) == d:
            count += 1
        i += 1
print(count)

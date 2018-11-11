# http://codeforces.com/problemset/problem/551/A
number_of_students = int(input())
students = list(map(int, input().split()))

sorted_students = sorted(students, reverse=True)
sorted_positions = []
count = 1
pre_count = 0
pre_student = sorted_students[0]
# using hashtable or create an array to store position of this sorted array
mapping = {}
# O(n)
for student in sorted_students:
    if student != pre_student:
        count += pre_count
        pre_count = 1
        mapping[student] = str(count)
        pre_student = student
        continue
    else:
        mapping[student] = str(count)
        pre_count += 1

positions = []
# O(n)
for student in students:
    positions.append(mapping[student])

print(' '.join(positions))
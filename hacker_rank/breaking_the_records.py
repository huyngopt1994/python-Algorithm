# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
number_records = int(input())

records = list(map(int, input().split()))

# expect we will show the number of breaking records and least records
count_breaking = 0
count_least = 0
current_max = records[0]
current_min = records[0]

for record in records[1:]:
    if record > current_max:
        count_breaking += 1
        current_max = record
    elif record < current_min:
        count_least += 1
        current_min = record

print('{} {}'.format(count_breaking, count_least))

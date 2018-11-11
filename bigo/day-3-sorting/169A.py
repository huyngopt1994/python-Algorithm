n, a, b = list(map(int, input().split()))
sorted_chores = sorted(list(map(int, input().split())))
count = 0
start_index = b - 1
if start_index < 0:
    start_index = 0
count = sorted_chores[start_index + 1] - sorted_chores[start_index]
if count < 0:
    count = 0
print(count)

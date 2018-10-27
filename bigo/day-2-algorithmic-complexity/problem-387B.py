number_of_n, number_of_m = list(map(int, input().split()))

numbers_n = list(map(int, input().split()))

numbers_m = list(map(int, input().split()))
index = 0
total_existed = 0
for i in range(number_of_n):
    count = 0
    while index < number_of_m:
        if numbers_n[i] <= numbers_m[index]:
            total_existed += 1
            # increase index here because we find a fixed problem
            index += 1
            break
        index += 1

print(number_of_n - total_existed)

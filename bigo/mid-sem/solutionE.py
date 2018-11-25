number_of_array = int(input())

my_list = list(map(int, input().split()))

my_list = sorted(my_list)
the_index_of_median = number_of_array // 2

print(my_list[the_index_of_median])

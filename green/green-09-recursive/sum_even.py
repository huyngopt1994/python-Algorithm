# get the sum of even numbers
import sys
sys.setrecursionlimit(10100)
def get_sum_even_numbers(array,count):
    if count <0:
        return 0
    if array[count] % 2 ==0:
        return array[count] + get_sum_even_numbers(array,count-1)
    else:
        return get_sum_even_numbers(array, count-1)

n = int(input())
my_array = list(map(int, input().split()))

result = get_sum_even_numbers(my_array,len(my_array)-1)

print(result)
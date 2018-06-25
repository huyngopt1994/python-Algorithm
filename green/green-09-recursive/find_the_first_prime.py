import sys
sys.setrecursionlimit(10001)
n =int(input())
my_input = list(map(int, input().split()))

def is_prime(number):
    if number <2 :
        return False
    flag = True
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            flag = False
            break
    return flag

def get_first_prime(your_list, count, max_length):
    if count > max_length:
        return -1
    elif is_prime(your_list[count]):
        return count
    else:

        return get_first_prime(your_list,count+1, max_length)

print(get_first_prime(my_input,0,len(my_input)-1))
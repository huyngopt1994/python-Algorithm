# Using recursion to calculate the numbers, 475 => return 3 , 1242 => 4
# stack for input 345 => (345,0) => (345,0) (34,1) => (345,0) (34,1) (3,2) =>(345,0) (34,1) (3,2) (0,3)(!Ping we got this)
def count_number(number):
    if number // 10 == 0:
        return number
    else:
        return count_number(number//10)

my_input = int(input())

result =  count_number(abs(my_input))

print(result)
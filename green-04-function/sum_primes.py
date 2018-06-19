
def is_prime(number):
    if number <2:
        return False
    flag = True

    for i in range(2, int(number**(0.5))+1):
        if number % i ==0:
            flag =False
    return flag


your_number = int(input())
sum = 0

for i in range(your_number):
    if is_prime(i):
        sum +=i
print(sum)
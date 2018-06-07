import math
def is_prime(number):
	is_prime =True
	# step 1 check case 1
	if number <= 1:
		is_prime = False
	else:
		# step 2 , set inital value is True
		is_prime = True
		for i in range(2, int(math.sqrt(number))+1):
			if number %i ==0:
				is_prime =False
				break
	return is_prime

my_number = int(input())
array_number = map(int, input().split())
count = 0
for number in array_number:
	if is_prime(number):
		count +=1

print(count)
"""
Description : Given a 32 bit signed interger , reverse digits of an integer
for example : -123 -> -321 ; 123 -> 321 ; 120 -> 21
**NOTE :  we couldlyu store integers within 32bit signed interger range: [-2^31, 2^32-1] => out  of this , please return 0

"""

"""
Some question : the way we  reverse
"""
# Solution1, convert this number string and swap them => cast it into int
# Time Complexity : O(n) , space complexity : O(1)
def reverse(number):
	#cast it into string
	input_string = list(str(number))
	len_input = len(input_string)
	if input_string[0] == '-':
		# negative ,please  keep it , just try to swap from input_string[1:]
		# get the middle:
		middle = (len_input-1) // 2
		print(middle)
		for i in range(1, middle+1): #loop n
			temp = input_string[len_input-i] # O(1)
			input_string[len_input-i] = input_string[i] #O(1)
			input_string[i] = temp #O(1)

	else:
		middle = (len_input) // 2
		for i in range(0, middle):
			temp = input_string[len_input-1-i]
			input_string[len_input-1-i] = input_string[i]
			input_string[i] = temp

	result = int(''.join(input_string))
	if -2**31 <= result <=2**32 -1:
		pass
	else:
		result =0
	return result

# Solution 2 , reverse int using functionality of list => Seem We can improve so much but the code 's more clear
def reverse_2(number):
	if number <0 :
		# negative ,please  keep it , just try to swap from input_string[1:]
		# get the middle:
		result = -1 * int(str(-number)[::-1])
	else:
		result = int(str(number)[::-1])

	if (result < -2 ** 31) or (result > 2 ** 31 - 1):
		result = 0
	return result



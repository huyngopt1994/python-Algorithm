""" Input : given array numbers , return indices of the two numbers such that they add up to a specific target
Assumption : each input => each one solution,  you may not use the same element twice

"""

# Solution1 : try to loop from first to the middle => choose a number and check it
# This is alogirthm for O(n^2) (time complexity) , 0(1) => Because they just require space for target and 2 variables

def loop(my_array , target):
	len_array = len(my_array)
	for i in range(0,len_array-1):
		for j in range(i+1,len_array):
			if (my_array[i] + my_array[j]) == target:
				return [i,j]


# Solution2:(Better) two pass hash table , Improve a little , instead of try to loop in the rest of array to check, Using hash table to reduce
# lookup time from O(n) -> O(1) by trading space for speed
# Time commplexity: 0(n) ( we traverse list twice , and hashtable reduces the look up time to O(1)
# Space complexity: O(n) : the extra space required depends on the number of items stored in the hash table,
#  which store exactly n elements
def using_hash_table(nums, target):
	# create dictionary to store my array firstly
	my_dict = {}
	# first iteration to store my array to  a hash table(dictionary)
	for i, value in enumerate(nums):
		my_dict[value] = i

	# second iteration
	for i in range(0, len(nums)):
		complement = target - nums[i]
		value = my_dict.get(complement, None)
		if value is not  None and value !=i:
			return [i, value]

# Solution3 : One pass hash table, the best instead do two things
# firstly , store in dictionary and loop to check the result => we will do anything in one loop
def using_one_pass_hash_table(nums, target):
	my_dict = {}

	for i , value  in enumerate(nums):

		# get the complement :
		complement = target - value
		check_value = my_dict.get(complement, None)
		if check_value is not None:
			return [value, i]

		# add into  dict:
		my_dict[value] = i




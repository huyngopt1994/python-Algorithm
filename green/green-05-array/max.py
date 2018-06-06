number = input()
array_number =list(map(float, input().split()))

max = array_number[0] # O(1)
for i in array_number:
	if i>= max: # O(n)
		max = i

print(max)
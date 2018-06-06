number = input()
array_number = map(int, input().split())
for i in array_number: #O(n)
	if i %2 ==0:
		print(i)

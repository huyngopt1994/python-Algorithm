# Verify requirement:
# input a list of number(height of flowers)
# Output : find total energy = sum( difference between the shorest flower and another flowers)
# Solution :
# 1./ find the shortest and the sum the height of flowers
# 2./ calculate the the energy = sum the height of flowers - (shortest* the number of flower))

number_flowers = int(input())

array_flower = list(map(int,input().split()))

min_flower = array_flower[0]
sum = 0

for flower in array_flower:
	if flower <= min_flower:
		# find the min
		min_flower =flower
	# calculate the sum
	sum += flower
result = sum - min_flower*number_flowers
print(result)
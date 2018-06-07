# output (requirement:
# 1./ find the basket  which has the max of apple
# 2./ if we have multiple baskets which have same the apple, choose the table of the max orange
# Solution: Find baskets which have max of apple
# in them we continue to check the max
number = int(input())
# We will store in 2 dimension matrix to store packet
def solution_1(number):

	packets = []
	max_apple = 0
	for i in range(1,number+1): #O(n)
		packet = list(map(int,input().split())) #O(2)
		if packet[0] == packet[1]:
			#please skip this basket
			continue
		else:
			# find the max apple
			if packet[0] >= max_apple:
				max_apple = packet[0]
			# add index to this packet
			packet.append(i)
			packets.append(packet)

	# So right now, we will get all packets which got the max apple , and try to get the
	max_apples = []

	max_orange= 0
	for packet in packets: #O(n)
		if packet[0] == max_apple:
			if max_orange < packet[1]:
				max_orange = packet[1]
			max_apples.append(packet)

	for packet in max_apples:
		if packet[1] == max_orange:
			print(packet[2])
			break

# This is algorithm for O(n)

def solution_2(number):
	#sort 2 dimension array using python
	packets = []
	for i in range(1,number+1): #O(n)
		packet = list(map(int,input().split())) #O(2)
		if packet[0] == packet[1]:
			#please skip this basket
			continue
		else:
			# add index to this packet
			packet.append(i)
			packets.append(packet)

	# please sort  packets follow apple( first element(number of apple) and second (number of orange))
	# in case we sort with 2 element so we will sort using tuple
	sorted_result = sorted(packets, key= lambda x: (x[0],x[1]), reverse = True)
	# big O : n log(n)
	print(sorted_result[0][2])

#solution_1(number)
solution_2(number)
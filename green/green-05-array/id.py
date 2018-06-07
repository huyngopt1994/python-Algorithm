number = int(input())
array_seat = list(map(int, input().split()))
#the output : export the minimum of staff's id
# solution :
# step1: sort the list firstly(ascending)
# step2: try to find where the minimum miss number
# solution : compare the input array with right array( 1, 2 ,3 ,4 ,5,6) => just use this refernce  array to figureout what the
# minimum seat

array_seat.sort()
minimum = 1
for seat in array_seat:
	if seat == minimum:
		minimum +=1
	else:
		break

print (minimum)
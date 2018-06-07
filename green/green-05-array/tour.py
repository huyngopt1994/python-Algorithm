number = int(input())
array_student = map(int, input().split())

# ouput : print "YES" if the number of man == number of woman
# solution : we just loop per student and count the number of man and number of woman and compare them

number_man = 0
number_woman = 0

for student in array_student:
	if student:
		number_man +=1
	else:
		number_woman +=1

if number_man == number_woman :
	print('YES')
else:
	print('NO')
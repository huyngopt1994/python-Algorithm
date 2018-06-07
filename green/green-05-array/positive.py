number = input()
array_number = map(int,input().split())

positive = True

for i in array_number:
	if i <= 0 :
		positive =False
		break

if positive:
	print ('YES')
else:
	print('NO')
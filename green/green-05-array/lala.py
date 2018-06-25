num_hour = int(input())

hours = list(map(int, input().split()))
flag = True
# 0 meaning learn computer, 1 learn english
# rule , we can have 0000 ( continuosly)
count = 0
for hour in hours:
    if hour == 0:
        count +=1
    else:
        count =0 #reset for next check

    if count ==4:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
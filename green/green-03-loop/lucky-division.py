"http://codeforces.com/problemset/problem/122/A"
#technic flag

s = input()

def verify_contain_lucky_number(s):
    flag = True
    for c in s:
        if c not in ['4', '7']:
            flag = False
            break
    return flag
flag =False
for i in range(1,1001):
    if verify_contain_lucky_number(str(i)):
        if int(s) % i == 0 :
            flag = True
            break

if flag:
    print('YES')
else:
    print('NO')
def verify_symmetry(your_string):
    # using flag to check
    flag = True
    len_your_string = len(your_string)

    mid = len_your_string//2

    for i in range(mid+1):
        if your_string[i] != your_string[len_your_string-1-i]:
            flag = False
            break
    return flag

result = verify_symmetry(input())
if result:
    print('YES')
else:
    print('NO')
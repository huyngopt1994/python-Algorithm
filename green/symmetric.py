"""
5 :
0 1 2 3 4

4 :
0 1 2 3

"""

n = input()
len_input = len(n)
middle = len_input // 2
is_symmetric = True
for i in range(0,middle+1):
    if n[i] != n[len_input-1-i]:
        is_symmetric = False


if is_symmetric:
    print('YES')
else:
    print('NO')
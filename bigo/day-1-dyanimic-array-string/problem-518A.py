# http://codeforces.com/problemset/problem/518/A
# We just think compare a string like a number, understand the special case to cover this .
import string

reference_string = list(string.ascii_lowercase)
s = list(input())
t = input()
len_number = len(s)

result = ""
is_good = False

for index in range(len_number - 1, -1, -1):
    if s[index] != 'z':
        refer_index = reference_string.index(s[index])
        refer_index += 1
        s[index] = reference_string[refer_index]
        break
    elif s[index] == 'z':
        s[index] = 'a'
s = ''.join(s)
if s == t:
    print('No such string')
else:
    print(s)

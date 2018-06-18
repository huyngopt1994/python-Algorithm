"""
Input: 'axav'
output : 'AxaV'
"""
n = input()

def uppercase(my_string):
    # because string is immutable so we have to create a new string and copy it
    res= ''
    for index,c in enumerate(my_string):
        if index == 0 or index == len(my_string)-1:
            if  'a'<=c <= 'z':
                c = chr(ord(c)-32)
        res += c
    return res
for _ in range(int(n)):
    my_string = input()
    res = uppercase(my_string)
    print(res)
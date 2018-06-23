def edit_string(my_string):
    capital_c = True
    result = ''
    for c in my_string:
        if c != ' ' and capital_c :
            if 'a' <= c <='z':
                c = chr(ord(c) - 32)
            capital_c =False
        elif c == ' ':
            capital_c = True
        else:
            if 'A' <= c <= 'Z':
                c = chr(ord(c) +32)
        result +=c
    print(result)

n = int(input())
for i in range(n):
    edit_string(input())
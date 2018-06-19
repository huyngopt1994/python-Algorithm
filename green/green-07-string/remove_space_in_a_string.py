def remove_space(my_string):
    # because string is immutable so we have to create a new string and copy it
    res= ''
    need_a_space = False
    for c in my_string:
        if c !=' ':
            if need_a_space:
                res += ' '
                need_a_space = False
            res += c
        elif len(res)>0 and res[-1] != ' ':
            need_a_space = True
    return res
my_string = input()
res = remove_space(my_string)
print(res)
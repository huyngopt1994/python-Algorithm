n = input()

def verify_this_string_contain(my_string):
    # technic set flag
    flag = False
    for c in my_string:
        if c.lower() in ['b', 'i', 'g', 'o']:
            flag = True
            break
    return flag

for _ in range(int(n)):
    my_string = input()
    if verify_this_string_contain(my_string):
        print('%s contain' % my_string)
    else:
        print('%s doesn"t containt '% my_string)
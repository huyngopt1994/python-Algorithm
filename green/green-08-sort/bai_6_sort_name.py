def is_smaller(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)
    if len_string1 < len_string2:
        use_len = len_string1
    else:
        use_len = len_string2
        # use len _string 1 to compare
    is_smaller = True
    for i in range(use_len):
        if string1[i] > string2[i]:
            return False
        elif string1[i] < string2[i]:
            return True

    return is_smaller

def buble_sort(names):
    for i in range(len(names) -1):
        for j in range(i+1, len(names)):
            if not is_smaller(names[i], names[j]):
                # Swap them
                temp = names[i]
                names[i] = names[j]
                names[j] = temp
    return names





number = int(input())

names = []
for _ in range(number):
    name = input()
    names.append(name)

names = buble_sort(names)
for name in names:
    print(name)
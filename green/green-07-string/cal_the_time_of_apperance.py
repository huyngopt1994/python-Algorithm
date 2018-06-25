def count_number(my_string):
    # first we will store
    unique_dict = {}
    for ch in my_string: #(O(n)
        ch_lower = ch.lower()
        if unique_dict.get(ch_lower,None):
            unique_dict[ch_lower] +=1
        else:
            unique_dict[ch_lower]= 1

    result =[]
    min_value = min(unique_dict.values()) #(O(n)
    for key, value in unique_dict.items(): # O(n)
        if value == min_value:
            result.append(key)

    #O(k)
    min_character = result[0]
    for ch in result:
        if ch < min_character:
            min_character = ch
    print(min_character.upper())

n = int(input())

for _ in range(n):
    my_input  = input()
    count_number(my_input)







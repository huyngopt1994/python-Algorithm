def count_number(my_string):
    # first we will store
    count = 0
    unique_dict = {}
    for ch in my_string: #O(n)
        if unique_dict.get(ch,None): #O(1)
            unique_dict[ch] +=1
        else:
            unique_dict[ch]= 1
            count +=1

    print(count)

# Call O(n) ,space complexity : O(k)
my_input  = input()
count_number(my_input)
def upper_case(my_string):
    upper = True
    new_string = ""
    for i in range(len(my_string)):
        c = my_string[i]
        if c =='.':
            if (i<len(my_string)-1) and (my_string[i+1] ==' '):
                upper= True
       # if c == ' ' and len(new_string) > 0 and new_string[-1] ==' ':
      #      continue
        elif upper and c != ' ' and c != '.':
            if 'a' <= my_string[i] <= 'z':
                c = chr(ord(c) -32)

            upper = False

        new_string += c

    print(new_string)

# Call O(n) ,space complexity : O(k)
my_input  = input()
upper_case(my_input)
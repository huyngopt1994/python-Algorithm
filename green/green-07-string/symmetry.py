def symmetry(my_string):
    new_string = ""
    word=""
    add_True = True
    for c1 in range(len(my_string)-1,-1,-1): #O(n)
        # handle case  within word
        if (my_string[c1] == ' ') and add_True:
            if len(new_string) !=0:
                # ye this the first word , so you don't need to add space
                new_string += ' '
            new_string += word
            word =''
            add_True =False
        elif c1==0: # ok we have to move to the last word
            word = (my_string[c1] + word)
            new_string += ' '
            new_string += word
        else:
            # we will collect char
            word = (my_string[c1] + word)
            add_True= True
    print(new_string)
## This is O(n) algorithm
my_input  = input()
symmetry(my_input)
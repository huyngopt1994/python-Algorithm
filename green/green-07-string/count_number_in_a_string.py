
def count_numeric_characters(my_string):
    # technic set flag
    count = 0
    for c in my_string:
        if c.isdecimal():
            count +=1
    return count

my_string = input()
count = count_numeric_characters(my_string)
print(count)
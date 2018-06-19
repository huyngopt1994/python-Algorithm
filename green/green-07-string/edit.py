def edit_string(my_string):
    capital_c = True
    result = ''
    for c in my_string:
        if c != ' ' and capital_c :
            c = c.upper()

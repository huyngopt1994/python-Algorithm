# apply a,b : a**b using (a*a*a*a (b times))
def get_exponent(a,b):
    #base case
    if b ==0:
        return 1
    #recursive case
    return a*get_exponent(a,b-1)

result = get_exponent(4,5)
print(result)

def fac(n):
    # base case
    if n <2:
        return 1
    # recursive case
    # it will call it your self but with smaller vallue
    return n*fac(n-1)

print(fac(4))
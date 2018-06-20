def gcd(a, b):
    # base case
    if b == 0:
        return a
    # recursive case
    r = a %b
    return gcd(b,r)

result = gcd(12,18)
print(result)
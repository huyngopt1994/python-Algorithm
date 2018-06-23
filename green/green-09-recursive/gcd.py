def gcd(a, b):
    # base case
    if b == 0:
        return a
    # recursive case
    r = a %b
    return gcd(b,r)

a, b = map(int,input().split())
print(gcd(a,b))
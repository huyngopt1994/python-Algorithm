# using euclid algorithm is an efficiently method for computing the greatest divisor(gcd) of two numbers
# greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number
# case a >b :  step 1 : r = a %b => a => will be get the smaller , b=> r
# case a <b ; r = a%b =a => a =b ; b= a  => it will be in case a >b
# we will keep this until  a % b == 0 => so we found the first gcd =>the greatest
def gcd(a,b):
    while b >0:
        r = a % b
        a = b
        b= r

    return a

c, d = map(int,input().split())

gcd = gcd(c,d)
c = c// gcd
d= d // gcd
print(c,d, sep=' ')
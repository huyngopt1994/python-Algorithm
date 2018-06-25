# We will use Euclid Algorithm to find the greatest gcd  between 2 numbers in 2 ways
def find_greatest_using_loop(a, b):
    # we just => convert a ,b => the lower and modulus
    while b > 0 :
        r = a % b # find modulus between 2 number
        a =b #update
        b =r # update
    return a

def find_greatest_using_recur(a, b):
    if b ==0 :
        return a
    # update a = b; b = (a %b)
    return find_greatest_using_recur(b, a%b)

print(find_greatest_using_loop(12,18))


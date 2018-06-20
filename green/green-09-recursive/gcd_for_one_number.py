def gcd(num1, num2):
    if num1 % num2 == 0 and num2 %2 !=0 :
        return num2
    return gcd(num1, num2-2)

a = int(input())
if a %2 ==0:
    result = gcd(a,a-1)
else:
    result = gcd(a,a-2)
print(result)

import sys
sys.setrecursionlimit(500001)
def gcd(num1, num2):
    if (num1 % num2 == 0) and (num2 %2 ==1) :
        return num2
    else:
        return gcd(num1, num2-2)

a = int(input())
if a %2 == 0:
    result = gcd(a,a-1)
else:
    result = a
print(result)
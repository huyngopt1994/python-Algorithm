def fibonaci(n,num1, num2):
    if n <2:

        return num2
    else:
        return fibonaci(n-1, num2,num1+num2)

my_input = int(input())

print(fibonaci(my_input,1,1))
"http://codeforces.com/problemset/problem/300/A"
number = int(input())
negative = []
positive = []
zero = []

numbers = input().split()
for number in numbers:
    if int(number) <0:
        negative.append(number)
    elif int(number)>0:
        positive.append(number)
    else:
        zero.append(number)

if len(positive) == 0:
    positive.extend(negative[-1:-3:-1])
    del negative[-1]
    del negative[-1]

if len(negative) %2 == 0:
    zero.append(negative[-1])
    del negative[-1]

print ('%s %s'% (len(negative), ' '.join(negative)))
print ('%s %s'% (len(positive), ' '.join(positive)))
print ('%s %s'% (len(zero), ' '.join(zero)))
"http://codeforces.com/contest/617/problem/A"
position = int(input())

step = 0
while position > 0:
    if position > 4:
        position -=5
    elif position> 3:
        position -= 4
    elif position >2:
        position -= 3
    elif position >1:
        position -= 2
    else:
        position -= 1
    step +=1
print(step)
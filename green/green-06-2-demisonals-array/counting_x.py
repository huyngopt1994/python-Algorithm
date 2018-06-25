m, n, x = map(int, input().split())

count = 0

arr = []
for i in range(m):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

for row in arr:
    for e in row:
        if e == x:
            count +=1

print(count)

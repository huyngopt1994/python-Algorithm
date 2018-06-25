import time
m,n = map(int, input().split())
a,b, p  = map(int,input().split())
arr = []
pre = a
current =b
start_time = time.time()

for i in range(m):
    tmp =[]
    for j in range(n):
        if (i==0 and j ==0):
            new_item = a
        elif(i==0 and j ==1):
            new_item =b
        else:
            new_item = (pre+ current) % p
            #update value
            pre = current
            current = new_item
        tmp.append(new_item)
    arr.append(tmp)


for item in arr:
    print(' '.join(list(map(str,item))))


# find the special(which the max of row and is min of column)
import time
m,n = map(int, input().split())
count = 0
arr = []
for i in range(m):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
start_time = time.time()
for i in range(m): #n
    # find the max in row
    max_value = max(arr[i]) #n
    max_col_indexes = []
    for j in range(n): #n
        if arr[i][j] == max_value:
            max_col_indexes.append(j)
    # ok we found the max element for this row:
    # check if it's min or not

    for col_index in max_col_indexes:
        flag = True
        for i in range(m):
            if arr[i][col_index] <max_value:
                flag= False
                break
        if flag:
            count +=1
print(time.time()-start_time)
print(count)

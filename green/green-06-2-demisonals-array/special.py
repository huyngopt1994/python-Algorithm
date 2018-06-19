# find the special(which the max of row and is min of column)

m,n = map(int, input().split())

count = 0

arr = []
for i in range(m):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

for index, row in enumerate(arr):
    # find the max in row
    max_value = max(row)
    max_col_indexes = []
    for col_index, data in enumerate(row):
        if data == max_value:
            max_col_indexes.append(col_index)
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

print(count)

m= int(input())

count = 0

arr = []
for i in range(m):
    tmp = list(map(int,input().split()))
    arr.append(tmp)

def check_diagnol(row_index, col_index, value):
    # so we have to verify the diagnol
    flag = True
    count = 0
    # Verify upper row
    for i in range(row_index-1,-1,-1):
        count +=1
        # verify left col
        if (col_index-count) >=0 and (arr[i][col_index-count] > value):
            flag = False
            return flag
        #verify right col
        if (col_index+count) <m and (arr[i][col_index+count] > value):
            flag = False
            return flag
    count = 0
    for i in range(row_index+1, m):
        count += 1

        if (col_index - count) >= 0 and (arr[i][col_index - count] > value):
            flag = False
            return flag

        if (col_index + count) < m and (arr[i][col_index + count] > value):
            flag = False
            return flag
    return flag

for index, row in enumerate(arr):
    # find the max in row
    max_value = max(row)
    max_col_indexes = []
    # look up follow the row
    for col_index, data in enumerate(row):
        if data == max_value:
            max_col_indexes.append(col_index)

    # look up follow the column
    for col_index in max_col_indexes:
        flag = True
        for i in range(m):
            if arr[i][col_index] > max_value:
                flag = False
                break
        if flag:
            if check_diagnol(index,col_index,arr[index][col_index]):
                count +=1

print(count)

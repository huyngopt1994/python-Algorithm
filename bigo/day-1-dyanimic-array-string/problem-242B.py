# http://codeforces.com/problemset/problem/242/B
"""
We will try to get all indexs of segment has min start , and max value of end
just loop per index of segment which have min start , if they has end value is equal with max value of end => break
=> we find it / this algo is O(n)
"""

num_segments = int(input())
start_segments = []
end_segments = []


def find_max_of_end(my_list): # O(n)
    max = my_list[0]
    for index, item in enumerate(my_list):
        if item > max:
            max = item
    return max


def find_index_of_min(my_list): #O(n)
    min = my_list[0]
    min_indexs = []
    for index, item in enumerate(my_list):
        if item < min:
            min = item
    for index, item in enumerate(my_list):
        if item == min:
            min_indexs.append(index)
    return min_indexs


for _ in range(num_segments):
    start, end = list(map(int, input().split()))
    start_segments.append(start)
    end_segments.append(end)

min_start_indexes = find_index_of_min(start_segments)
max_end = find_max_of_end(end_segments)
result = -1
for index in min_start_indexes: #O(n)
    if end_segments[index] == max_end:
        result = index
        break
if result == -1:
    print(result)
else:
    print(result + 1)


"""The second way :
1. find max of end
2. find min of start
3. loop per element check if the element has end = max and min = start"""
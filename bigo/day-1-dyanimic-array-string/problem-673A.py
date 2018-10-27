# http://codeforces.com/problemset/problem/673/A
number_of_interested_times = int(input())
interested_times = list(map(int, input().split()))
result = 0


def get_interested_time():
    if number_of_interested_times == 1:
        if interested_times[0] > 15:
            return 15
        else:
            return (interested_times[0] + 15)
    pre_intertesed_time = 0

    for interested_time in interested_times:
        if interested_time - pre_intertesed_time <= 15:
            pre_intertesed_time = interested_time
        else:
            pre_intertesed_time += 15
            return pre_intertesed_time
    pre_intertesed_time += 15
    if pre_intertesed_time > 90:
        pre_intertesed_time = 90
    return pre_intertesed_time


# second way , we need to think the way of more general not find a solution
# for checking per case depend result like this
"""
Start to use 0  for the start and the end 
loop from the second to end , if  i - (i-1) >15 => prin (i-1) +15
if result > 90 => print 90
"""


def get_interested_time_second_way():
    interested_times.insert(0, 0)
    for index in range(len(interested_times)):
        if index == 0:
            continue
        if interested_times[index] - interested_times[index - 1] > 15:
            return interested_times[index - 1]
    return interested_times[-1]


result = (get_interested_time_second_way() + 15)
if result > 90:
    result = 90
print(result)

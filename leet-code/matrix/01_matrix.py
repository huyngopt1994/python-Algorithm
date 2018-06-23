"https://leetcode.com/problems/01-matrix/description/"
from collections import deque
n= int(input())
a = []
for i in range(n):
    tmp  = list(map(int, input().split()))
    a.append(tmp)

def solution_1(my_input):
    # Time complexiy
    num_row = len(my_input)
    num_col = len(my_input[0])
    # step 1: initilize data

    result = [[10000]*num_col for _ in range(num_row)]
    for i in range(num_row):
        for j in range(num_col): # big(0) : O(n^2*r^2)
            # so we will check per element in matrix to calculate the nearest distance
            if my_input[i][j]==0:
                result[i][j] = 0
            else:
                # we have to look up again every element to find the min distance
                for i1 in range(num_row):
                    for j1 in range(num_col):
                        if my_input[i1][j1] ==0 and (abs(i1-i) + abs(j1-j)) < result[i][j]:
                            print(abs(i1-i) + abs(j1-j))
                            result[i][j] = (abs(i1-i) + abs(j1-j))

    return result

def solution_with_bfs(matrix):
    # Using breath first search to search
    #create queue for using breath first search
    # firstly all zero is level 1 , 1 around 0 is level 2, 1 around 1 level 3
    searched_queue = deque()

    num_row = len(matrix)
    num_col = len(matrix[0])

    #first create result which store distance

    result = [[10000] * num_col for _ in range(num_row)]
    # so we have a new result matrix with  10000 default value
    # loop and edit result and add to the queue
    for i in range(num_row):
        for j in range(num_col):
            if (matrix[i][j] ==0):
                # if matrix[i][j] =0 we will set result =0 and add it like a node to queue
                result[i][j] = 0
                searched_queue.append([i,j])

    # make a queue just include cell which have value 0

    # [row,column] => [left, right, up, down]
    adjacent_list= [[0,1],[0,-1],[1,0],[-1,0]]
    # this case is a little different
    while searched_queue: # loop a queue
        # first we have to pop a cell
        cell = searched_queue.popleft() #pop cell
        current_row = cell[0]
        current_col = cell[1]
        # ok now we have to look up adjacent nodes (maybe this is 1 near it)
        # find to lookup 1 cell
        for i in adjacent_list:

            new_row = current_row + i[0]
            new_col = current_col + i[1]


            if (new_row >= 0 and new_col >= 0 and new_row < num_row and new_col < num_col):
                # ok this adjacent node is still  in matrix

                if (result[new_row][new_col] > (result[current_row][current_col])):
                    #
                    #ok we found cell 1,please calculate and update it
                    # if 0 found 1 => this 1 => will get distance (0+1)
                    # if 1 find 1 => this 1 => will get current_distance +1, if any zero
                    result[new_row][new_col] = (result[current_row][current_col] + 1)
                    # after that we add "1" to verify if we found any "1" near it
                    searched_queue.append([new_row,new_col])
    return result
print(solution_with_bfs(a))
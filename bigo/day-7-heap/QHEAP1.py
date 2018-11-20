# https://www.hackerrank.com/challenges/qheap1/problem?fbclid=IwAR3fWJHCKstUUT_oLYuMt7fmgc6ESSZRLkdklBMT_6YpewWz1ppb_TxWeeY
import queue

"""
Because it's task for building min heap I don't use library for it
try to build by myself
steps to build a min heap
constraints:
when we delete it always in heap and we just only contain distinct elements in heap
1. read data
# first case the min heap is empty
"""


def min_heapify(i, current_heap):
    smallest = i
    len_h = len(current_heap)
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len_h and current_heap[left] < current_heap[smallest]:
        # swap
        smallest = left
    if right < len_h and current_heap[right] < current_heap[smallest]:
        smallest = right
    if smallest != i:
        current_heap[i], current_heap[smallest] = current_heap[smallest], current_heap[i]
        min_heapify(smallest, current_heap)


def insert_a_node(node_value, current_heap):
    # it's quite easy
    # always add the last
    current_heap.append(node_value)
    len_heap = len(current_heap)
    if len_heap == 1:
        return current_heap
    else:
        # find the parent node:
        child_heap = len_heap - 1
        while child_heap != 0 and (current_heap[(child_heap - 1) // 2] > current_heap[child_heap]):
            # swap
            current_heap[(child_heap - 1) // 2], current_heap[child_heap] = current_heap[child_heap], current_heap[
                (child_heap - 1) // 2]
            # update
            child_heap = (child_heap - 1) // 2

    return current_heap


def pop(my_heap):
    length = len(my_heap)
    if length == 0:
        return
    my_heap[0] = my_heap[length - 1]
    my_heap.pop()
    min_heapify(0, my_heap)


# get index, it's a bad way to do it , for normal case we don't know


times = int(input())
my_heap = []
pg_remove = queue.PriorityQueue()
for _ in range(times):
    values = input().split()

    if values[0] == '1':
        insert_a_node(int(values[1]), my_heap)
    elif values[0] == '2':
        pg_remove.put(int(values[1]))
    else:
        while not pg_remove.empty() and my_heap[0] == pg_remove.queue[0]:
            # it existed in pg_remove
            # should remove all
            pop(my_heap)
            pg_remove.get()
        print(my_heap[0])

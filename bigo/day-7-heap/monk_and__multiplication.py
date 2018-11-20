"""
problem: https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/?fbclid=IwAR218NlpbCdt3tF4qJX5uUaTSkxWY8TWzp0a9hnRxxvukWTYlLuEUNnuYB0
solution:
in a list: we build a heap sort with 2 guys first (max heap)
after that we will build

"""
from queue import PriorityQueue

number = int(input())
numbers = list(map(int, input().split()))
if number < 3:
    for _ in len(numbers):
        print('-1')
else:
    # build min heap with first
    for _ in range(2):
        print('-1')
    mh = PriorityQueue()
    # first time
    product = 1
    for x in numbers[:3]:
        product *= x
        mh.put(x)
    print(product)

    for x in numbers[3:]:
        current_min = mh.queue[0]
        if x > current_min:
            # need to delete and update again
            mh.get() # get the first
            mh.put(x) #add the new and rearrange the heap
            product //= current_min
            product *= x
        print(product)

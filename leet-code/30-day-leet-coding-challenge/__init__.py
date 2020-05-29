from queue import Queue
from collections import OrderedDict


class FirstUnique:

    def __init__(self, nums):
        self.my_queue = Queue()
        self.hash_count = {}
        self.unique_items = OrderedDict()
        self.order_item = []
        for num in nums:
            self.add(num)
        self.prev_first_unique = 0

    def showFirstUnique(self) -> int:
        # O(n) for first case
        while self.unique_items:
            return next(iter(self.unique_items))
        return -1

    def add(self, value: int) -> None:
        self.my_queue.put(value)

        if value not in self.hash_count:
            self.hash_count[value] = 1
            # Just add unique
            self.unique_items[value] = 1
        else:
            if value in self.unique_items:
                del self.unique_items[value]
            self.hash_count[value] += 1

class MyMinHeap(object):
    def __init__(self, raw_data):
        self.heap = raw_data
        self._build_heap(len(self.heap))

    def _standard_min_heap(self, i, len_heap):
        smallest = i
        left = 2 * i + 1  # find the child node
        right = 2 * i + 2
        # update smallest
        if left < len_heap and h[left] < h[smallest]:
            smallest = left
        if right < len_heap and h[right] < h[smallest]:
            smallest = right

        # if smallest is change, should swap values between them. after update try to run recursive to check the left
        if smallest != i:
            h[smallest], h[i] = h[i], h[smallest]
            self._standard_min_heap(smallest, len_heap)

    def _build_heap(self, n):
        """O(n)"""
        for i in range(n // 2 - 1, -1, -1):
            self._standard_min_heap(i, n)

    def __str__(self):
        return str(self.heap)

    def min_node(self):
        """O(1)"""
        return self.heap[0]

    def add_node(self, new_node_value):
        """
        When we add a new_node_value , we add in the last of heap. find the parent node of new node
        check and swap , after that we just find the parent of the found node.

        :return:
        """
        self.heap.append(new_node_value)
        index = len(self.heap) - 1
        # find the parent node round down((i-1)//2)
        while index != 0 and self.heap[(index - 1) // 2] > self.heap[index]:
            # should swap value
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            # reupdate index
            index = (index - 1) // 2


if __name__ == '__main__':
    h = [7, 12, 6, 10, 17, 15, 2, 4]
    a = MyMinHeap(h)
    print(a)
    print(a.min_node())
    a.add_node(5)
    print(a)

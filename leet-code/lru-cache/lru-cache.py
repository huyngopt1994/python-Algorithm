class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(key=0, value=0)
        self.tail = Node(key=0, value=0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_head(self, key: int, value: int) -> Node:
        new_head = Node(key=key, value=value)
        current_head = self.head.next
        self.head.next = new_head
        new_head.next = current_head
        new_head.prev = self.head
        current_head.prev = new_head
        self.size += 1
        return new_head

    def remove_tail(self):
        if self.size == 0:
            return
        deleted_tail = self.tail.prev
        predecessor = self.tail.prev.prev
        predecessor.next = self.tail
        self.tail.prev = predecessor
        self.size -= 1
        return deleted_tail


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node_hash_map = {}
        self.my_linked_list = DoubleLinkedList()

    def remove_current_node(self, current_node):
        successor = current_node.next
        predecessor = current_node.prev
        predecessor.next = successor
        successor.prev = predecessor
        self.my_linked_list.size -= 1

    def get(self, key: int) -> int:
        # O(1)
        if key not in self.key_node_hash_map:
            return -1

        current_node = self.key_node_hash_map[key]
        self.remove_current_node(current_node)
        new_node = self.my_linked_list.add_head(key=current_node.key, value=current_node.value)

        self.key_node_hash_map[key] = new_node
        return new_node.value

    def put(self, key: int, value: int) -> None:
        # O(1)
        if key in self.key_node_hash_map:
            current_node = self.key_node_hash_map[key]
            self.remove_current_node(current_node)

        elif self.my_linked_list.size == self.capacity:
            # not in
            deleted_tail = self.my_linked_list.remove_tail()
            if deleted_tail:
                del self.key_node_hash_map[deleted_tail.key]

        new_node = self.my_linked_list.add_head(key=key, value=value)
        self.key_node_hash_map[key] = new_node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)  # evicts key 2
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    # Double linked list
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Index start from 0
        self.length = 0

        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # Check index is valid

        if index < 0 or index > self.length - 1:
            return -1

        # Check should start from the head or tail
        if index > self.length // 2:
            # Start from tail
            curr = self.tail
            # should traverse self.length-1 -self.index times
            for _ in range(0, self.length - index):
                curr = curr.prev
        else:
            # Start from sentinel head
            curr = self.head

            # should jump index times
            for _ in range(0, index + 1):
                curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val=val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current_length = self.length
        self.addAtIndex(current_length, val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # Check index
        if index < 0 or index > self.length:
            # invalid index
            return

        added_node = Node(val=val)
        if index == 0:
            # Add head
            successor = self.head.next
            self.head.next = added_node
            added_node.next = successor
            successor.prev = added_node
            added_node.prev = self.head
        elif index == self.length:
            # Add tail
            predecessor = self.tail.prev
            predecessor.next = added_node
            added_node.next = self.tail
            self.tail.prev = added_node
            added_node.prev = predecessor
        else:
            # Handle latter
            # Go to the (index -1) th node
            predecessor = self.head
            # index -1 times
            for i in range(0, index):
                predecessor = predecessor.next

            successor = predecessor.next
            predecessor.next = added_node
            added_node.next = successor
            successor.prev = added_node
            added_node.prev = predecessor

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.length - 1:
            return

        # I want to get (index -1) th
        predecessor = self.head
        for i in range(0, index):
            predecessor = predecessor.next

        successor = predecessor.next.next
        predecessor.next = successor
        successor.prev = predecessor

        self.length -= 1

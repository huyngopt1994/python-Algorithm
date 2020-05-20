class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    # Singular linked list
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Index start from 0
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # Check index is valid
        if index > self.length - 1:
            return -1
        # Check it's the head

        if index == 0:
            return self.head.val

        traversed_node = self.head
        # we should traverse index time because we start from zero
        # for example we want to access index 2 , so we need jump 2 times
        for i in range(1, index + 1):
            # next for index -1 times
            traversed_node = traversed_node.next

        return traversed_node.val

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
        if index > self.length:
            # invalid index
            return

        added_node = Node(val=val)
        if self.head is None:
            self.head = added_node
        elif index == 0:
            temp = self.head
            self.head = added_node
            self.head.next = temp
        else:
            # Go to the (index -1) th node
            traversed_node = self.head
            # index -2 times
            for i in range(1, index):
                traversed_node = traversed_node.next

            index_th_node = traversed_node.next
            traversed_node.next = added_node
            added_node.next = index_th_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self.length - 1:
            return

        if index == 0:
            # delete head node
            self.head = self.head.next
        else:
            # I want to get (index -1) th
            traversed_node = self.head
            # index -2 times
            for i in range(1, index):
                traversed_node = traversed_node.next

            # index-nth
            # update index -1 th .next to index +1 th
            traversed_node.next = traversed_node.next.next

        self.length -= 1

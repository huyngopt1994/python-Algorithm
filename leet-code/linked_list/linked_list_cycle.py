# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # just go slow  and go fast, if one of the node is reach to None => return false
        # If the node from go slow == go fast => loop => return True
        if head is None:
            return False
        slow_node = head
        fast_node = head
        while True:
            slow_node = self.go_slow(slow_node)
            fast_node = self.go_fast(fast_node)
            if (slow_node and fast_node) is None:
                return False
            if slow_node == fast_node:
                return True

    def go_slow(self, node: ListNode) -> ListNode:
        return node.next

    def go_fast(self, node: ListNode):
        if node.next is not None:
            return node.next.next
        return None

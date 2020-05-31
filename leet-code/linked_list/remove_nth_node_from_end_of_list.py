# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd_with_storing_array(self, head: ListNode, n: int) -> ListNode:
        # Need to store this linked list into an array
        stored_array = []
        current_node = head
        while current_node:
            stored_array.append(current_node)
            current_node = current_node.next
        if len(stored_array) == 1:
            return None
        pre_node = len(stored_array) - 1 - n
        successor = len(stored_array) + 1 - n
        if pre_node < 0:
            # Delete head
            return stored_array[1] if len(stored_array) > 1 else None

        successor = stored_array[successor] if successor < len(stored_array) else None
        stored_array[pre_node].next = successor
        return head

    def removeNthFromEnd_with_sliding_window_technic(self, head: ListNode, n: int) -> ListNode:
        right_node = head
        left_node = head
        # init the window we will make a window with n+1 (presssor => tail because we are only direction
        for _ in range(n):
            left_node = left_node.next
            if left_node is None:
                # delete head
                return head.next

        while left_node.next:
            right_node = right_node.next
            left_node = left_node.next

        right_node.next = right_node.next.next
        return head

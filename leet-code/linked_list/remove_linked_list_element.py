# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:  # case empty
            return None

        # Start 2 pointers pre and current
        pre_node = head
        post_node = head.next

        while post_node:
            # jump to check
            if post_node.val == val:
                # Remove it
                pre_node.next = post_node.next
                post_node = pre_node.next
            else:
                post_node = post_node.next
                pre_node = pre_node.next
        # Handle case delete at head
        if head.val == val:
            head = head.next
        return head

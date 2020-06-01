class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseListUsingIteration(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        original_head = head
        while original_head.next:
            next_head = original_head.next
            original_head.next = original_head.next.next
            next_head.next = head
            head = next_head
        return head

    def reverseListUsingRecursive(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        original_head = head
        return self.recursive(head, original_head)

    def recursive(self, head, original_head):
        if original_head.next is None:
            return head
        next_head = original_head.next
        original_head.next = original_head.next.next
        next_head.next = head
        head = next_head
        return self.recursive(head, original_head)

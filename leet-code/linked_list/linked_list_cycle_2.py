# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Using fold algorithm, first verify if it's intersect or not
        intersection = self.findIntersect(head)
        if intersection is None:
            return None
        start = head
        while start != intersection:
            start = start.next
            intersection = intersection.next
        return intersection

    def findIntersect(self, head: ListNode):
        if head is None:
            return None
        go_slow = head
        go_fast= head
        while True:
            go_slow = go_slow.next
            if go_fast.next is None:
                return None
            else:
                go_fast = go_fast.next.next
            if go_slow == go_fast:
                return go_slow
            if (go_slow and go_fast) is None:
                return None


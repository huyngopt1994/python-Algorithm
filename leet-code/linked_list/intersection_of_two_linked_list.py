class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # O(n) space complexity
        traversed_map = {}
        current_headA = headA
        while current_headA:
            traversed_map[current_headA.val] = current_headA
            current_headA = current_headA.next
        # Check
        current_headB = headB
        while current_headB:
            if current_headB.val in traversed_map:
                # start to check
                intersection_node = current_headB
                current_checkA = traversed_map[current_headB.val]
                while current_headB and current_checkA:
                    if current_headB != current_checkA:
                        break
                    current_headB = current_headB.next
                    current_checkA = current_checkA.next
                if current_headA is None and current_headB is None:
                    return intersection_node
            current_headB = current_headB.next

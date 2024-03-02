
# https://leetcode.com/problems/linked-list-cycle/
# all test passed
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False

    left = head
    right = head.next
    while right and right.next:
        if right == left:
            return True

        left = left.next
        right = right.next.next

    return False
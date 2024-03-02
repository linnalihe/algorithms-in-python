# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    sentinal = ListNode(0)
    sentinal.next = head
    left = sentinal
    right = head
    while right and n > 0:
        right = right.next
        n-=1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return sentinal.next
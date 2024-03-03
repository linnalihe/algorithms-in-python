# https://leetcode.com/problems/reorder-list/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # find the 2nd half of the list and reverse
    # then merge the first half and the second half

    if not head or not head.next:
        return head

    node1 = head
    node2 = head.next
    while node2 and node2.next:
        node1 = node1.next
        node2 = node2.next.next

    first = head
    second = node1.next
    node1.next = None

    prev = None
    while second and second.next:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    second.next = prev

    sentinal = ListNode(0)
    root = sentinal
    while second:
        sentinal.next = first
        sentinal = sentinal.next
        first = first.next
        sentinal.next = second
        sentinal = sentinal.next
        second = second.next

    if first:
        sentinal.next = first

    return root.next
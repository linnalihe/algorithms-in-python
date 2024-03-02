# https://leetcode.com/problems/reverse-linked-list/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
        
    prevnode = None
    curr = head
    while curr and curr.next:
        nextnode = curr.next
        curr.next = prevnode
        prevnode = curr
        curr = nextnode

    curr.next = prevnode
    return curr
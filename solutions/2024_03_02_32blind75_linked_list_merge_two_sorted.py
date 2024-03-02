# https://leetcode.com/problems/merge-two-sorted-lists/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    sentinal = ListNode(0)
    root = sentinal
    while list1 and list2:
        if list1.val <= list2.val:
            sentinal.next = list1
            list1 = list1.next
            sentinal = sentinal.next
            
        else:
            sentinal.next = list2
            list2 = list2.next
            sentinal = sentinal.next
            

    if list1:
        sentinal.next = list1
    if list2:
        sentinal.next = list2

    return root.next
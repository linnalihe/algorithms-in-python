# https://leetcode.com/problems/merge-two-sorted-lists/description/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinal = ListNode(0)
        currnode = sentinal

        while list1 and list2:
            if list1.val <= list2.val:
                currnode.next = list1
                list1 = list1.next
            else:
                currnode.next = list2
                list2 = list2.next
            
            currnode = currnode.next

        if list1:
            currnode.next = list1


        if list2:
            currnode.next = list2

        return sentinal.next
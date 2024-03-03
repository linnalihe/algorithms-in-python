# https://leetcode.com/problems/merge-k-sorted-lists/
# all tests passed
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    # bruteforce is to merge each list into the first one
    # O(k*m) where m is the length of the lists
    # can get O(n log k) by merging two lists at at time until they are all merged

    def mergetwo(idx1, idx2):
        sentinal = ListNode(0)
        root = sentinal
        list1 = lists[idx1]
        list2 = lists[idx2]
        while list1 and list2:
            if list1.val <= list2.val:
                sentinal.next = list1
                
                list1 = list1.next
            else:
                sentinal.next = list2
                list2 = list2.next

            sentinal = sentinal.next
        
        if list1:
            sentinal.next = list1

        if list2:
            sentinal.next = list2

        return root.next

    
    idx1 = 0
    idx2 = len(lists)-1

    while idx2 > 0:
        idx1 = 0
        while idx1 < idx2:
            
            lists[idx1] = mergetwo(idx1, idx2)
            idx1+=1
            idx2-=1

    return lists[0] if len(lists) > 0 else None
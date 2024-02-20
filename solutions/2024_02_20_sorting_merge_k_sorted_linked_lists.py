# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573731-921952-245-1546
# all tests passed

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_two_sorted_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1
        
    sentinal = LinkedListNode(0)
    currnode = sentinal
    
    while list1 and list2:
        if list1.value <= list2.value:
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


def merge_k_lists(lists):
    if not lists:
        return None
    # merge 2 lists at a time until there is only 1 list
    # space O(n * log k) where k is number of lists and n is total nodes
    # we need to look at n at most log k times
    
    left = 0
    right = len(lists)-1
    bound = len(lists)-1
    
    while bound > left:
        while left < right:
            lists[left] = merge_two_sorted_lists(lists[left], lists[right])
            left+=1
            right-=1
        
        left = 0
        bound = right
    
    return lists[0]
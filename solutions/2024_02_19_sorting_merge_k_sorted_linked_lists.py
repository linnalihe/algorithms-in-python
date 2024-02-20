import heapq

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # brute force to iterate n times where n is total number of nodes and pick smallest each time
    # O(n^2) time, O(n) space for output
    # better is to add all values to minheap and pull them out
    # time includes adding to array + heapify + pulling out => O(n) + O(n) + O(n log n) => O(n log n)
    # space is still O(n)
    # it's a min heap so we swap root with last and pop out last, put next element and heapify
    
    output = LinkedListNode(-1)
    currnode = output
    lists = [(each.value, idx, each) for idx, each in enumerate(lists) if each]
    heapq.heapify(lists)

    while lists:
        min_val, idx, min_val_node = heapq.heappop(lists)
        currnode.next = min_val_node
        currnode = currnode.next
        if min_val_node.next:
            heapq.heappush(lists, (min_val_node.next.value, idx, min_val_node.next))
        
    return output.next
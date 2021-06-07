# Intersection
# Given two singly linked lists, determine if the list intersects
# If they intersect, return the intersecting node

def sol_intersecting(node1: Node, node2: Node):
    if node1 == None or node2 == None:
        return None

    result1 = getTailAndSize(node1)
    result2 = getTailAndSize(node2)

    # if different tail nodes then there is no intersection
    if(result1.tail != result2.tail):
        return None

    # set pointers to the start of each linked list
    shorter = node1 if result1.size < result2.size else result2
    longer = node2 if result1.size < result2.size else node1

    # move the pointer for the longer list by difference in length
    longer = getKthNode(longer, abs(result1.size-result2.size))

    # move both pointers until intersection
    while(shorter != longer):
        shorter = shorter.next
        longer = longer.next

    # return either the longer or the shorter
    return longer


class Result:
    def __init__(self, tail: Node, size: int):
        self.tail = tail
        self.size = size


def getTailAndSize(inputlist: Node):
    if(inputlist == None):
        return None
    size = 1
    current = inputlist
    while(current.next != None):
        size += 1
        current = current.next
    return Result(current, size)


def getKthNode(head: Node, k: int):
    current = head
    while(k > 0 and current != None):
        current = current.next
        k -= 1
    return current

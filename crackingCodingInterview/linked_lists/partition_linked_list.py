# Partition
# Write code to partition a linked list around a value x such that all nodes less than x
# come before all nodes greater than or equal to x

# create a new linked list for smaller than and a new linked list for greater than
# iterate through the linked list
# if all nodes less than x, append to smaller
# if node is x increase counter
# if nodes greater than x, append to greater

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def partition(node: Node, x: int):

    xInNode = 0
    smaller = None
    greater = None

    while node:
        if(node.value < x):
            if smaller:
                smaller.next = Node(node.value)
                smaller = smaller.next
            else:
                smaller = Node(node.value)
                smallerRoot = smaller
        if(node.value > x):
            if greater:
                greater.next = Node(node.value)
                greater = greater.next
            else:
                greater = Node(node.value)
                greaterRoot = greater

    if xInNode > 0:
        for i in range(xInNode):
            smaller.next = Node(node.value)
            smaller = smaller.next

    smaller.next = greaterRoot

    return smallerRoot


def sol_partition(node: Node, x: int):
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    while node != None:
        next = node.next
        node.next = None
        if(node.data < x):
            if(beforeStart == None):
                beforeStart = node
                beforeEnd = beforeStart
            else:
                beforeEnd.next = node
                beforeEnd = node
        else:
            if(afterStart == None):
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node
        node = next
    if beforeStart == None:
        return afterStart

    beforeEnd.next = afterStart
    return beforeStart

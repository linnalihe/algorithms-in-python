# Palindrome
# Check if a linked list is a palindrome

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def sol_palindrome(head: Node):
    reversed = reverse_list(head)
    return is_equal(head, reversed)


def reverse_list(node: Node):
    head = None
    while(node != None):
        n = Node(node.value)
        n.next = head
        head = n
        node = node.next
    return head


def is_equal(node1: Node, node2: Node):
    while (node1 != None and node2 != None):
        if(node1.value != node2.value):
            return False

        node1 = node1.next
        node2 = node2.next

    return node1 == None and node2 == None


def sol2_palindrome(head: Node):
    fast = head
    slow = head

    stack = deque()

    # push elements from first half of linked list onto stack
    # when fast runner reaches end of list, slow will be be at the middle
    while (fast != None and fast.next != None):
        stack.push(slow.value)
        fast = fast.next.next

    if(fast != None):
        slow = slow.next

    while(slow != None):
        top = stack.pop().value
        if(top != slow.value):
            return False
        slow = slow.next

    return True

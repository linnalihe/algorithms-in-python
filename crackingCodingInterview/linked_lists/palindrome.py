# Palindrome
# Check if a linked list is a palindrome

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

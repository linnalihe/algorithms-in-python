# Kth to Last
# Implement an algorithm to find the kth to last element of a singly linked list

# iterate through the singly linked list to find the length
# iterate len(linkedlist) - k to get the kth to last element

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def kth_to_last(head: Node, k: int):
    p1 = head
    p2 = head
    for i in range(k):
        if(p1 == None):
            return None
        p1 = p1.next

    while(p1 != None):
        p1 = p1.next
        p2 = p2.next

    return p2.value


def sol_kth_to_last(head: Node, k: int):
    if(head == None):
        return 0

    index = sol_kth_to_last(head.next, k) + 1
    if(index == k):
        print(str(k)+"th to last: " + str(head.value))

    return index


if __name__ == "__main__":
    root = Node(5)
    root.next = Node(6)
    root.next.next = Node(7)
    root.next.next.next = Node(8)
    print(kth_to_last(root, 2))
    sol_kth_to_last(root, 2)

# Loop detection - Find start of loop
# Given a circular linked list, return the node at the beginning of the loop

def find_loop_start(head: Node):
    slow = head
    fast = head
    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            break

    if(fast == None or fast.next == None):
        return None

    slow = head
    while(slow != fast):
        slow = slow.next
        fast = fast.next

    return fast

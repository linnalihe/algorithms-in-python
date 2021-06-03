# Remove Dups
# Write code to remove duplicates from an unsorted linked list

# can use a hashmap or dictionary and then remove all the links that we've seen


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def remove_dups(root: Node):

    seen = dict()
    current = root
    while current.next:
        if seen.get(current.next.value, False):
            current.next = current.next.next
        seen[current.value] = True
        current = current.next


def sol_remove_dups(n: Node):
    seen = set()
    previous = None
    while(n != None):
        if n.value in seen:
            previous.next = n.next
        else:
            seen.add(n.value)
            previous = n

        n = n.next


def sol2_remove_dups(n: Node):
    current = n
    while(current != None):
        runner = current
        while(runner.next != None):
            if(runner.next.value == current.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


if __name__ == "__main__":
    root = Node(5)
    root.next = Node(6)
    root.next.next = Node(5)
    root.next.next.next = Node(1)

    current = root
    while current:
        print(current.value)
        current = current.next
    current = root
    sol2_remove_dups(current)
    print("---")
    while current:
        print(current.value)
        current = current.next

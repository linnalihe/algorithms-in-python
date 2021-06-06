# Sum List
# You have two numbers represented by a linked list, where each node contains a single digit
# Digits are stored in reverse order, 1's digit is at the head
# Return  a linked list where the nodes are the sum of the inputs
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next: Node):
        self.next = next


def sol_sum_list(node1: Node, node2: Node, carry: int):
    if node1 == None and node2 == None and carry == 0:
        return None

    value = carry
    if node1 != None:
        value += node1.value
    if node2 != None:
        value += node2.value

    result = Node(value % 10)

    if node1 != None or node2 != None:
        n1 = None if node1 == None else node1.next
        n2 = None if node2 == None else node2.next
        c = 1 if value >= 10 else 0
        more = sum_list(n1, n2, c)

        result.setNext(more)

    return result


class PartialSum:
    def __init__(self):
        p_sum = None
        carry = 0


def sol2_sum_list(node1: Node, node2: Node):
    len1 = len(node1)
    len2 = len(node2)

    # pad shorting list with zeros
    if(len1 < len2):
        node1 = padList(node1, len2 - len1)
    else:
        node2 = padList(node2, len1 - len2)

    # add lists
    p_sum = addListsHelper(node1, node2)

    # insert the carry at the front of the list if carry > 0, else return list
    if p_sum.carry == 0:
        return p_sum.p_sum
    else:
        result = insertBefore(p_sum.p_sum, p_sum.carry)
        return result


def addListsHelper(node1, node2):
    if(node1 == None and node2 == None):
        return PartialSum()

    # add smaller digits recursively
    p_sum = addListsHelper(node1.next, node2.next)

    # add carry to current data
    val = p_sum.carry + node1.value + node2.value

    # insert sum of current digits
    full_result = insertBefore(p_sum.p_sum, val % 10)

    # return p_sum with the updated p_sum and carry values
    p_sum.p_sum - full_result
    p_sum.carry = val / 10
    return p_sum

# pad list with zeros


def padList(node: Node, padding: int):
    head = node
    for i in range(padding):
        head = insertBefore(head, 0)
    return head


# insert node in front of linked list
def insertBefore(list: Node, data: int):
    node = Node(data)
    if list != None:
        node.next = list
    return node

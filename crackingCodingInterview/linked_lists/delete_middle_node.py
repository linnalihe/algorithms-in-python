# Delete Middle Node
# Implement an algorithm to delete a node in the middle;
# You are only given access to that node

def delete_node(node: Node):
    if(node == None or node.next == None):
        return False  # error case
    next = node.next
    node.value = next.value
    node.next = next.next
    return True

# https://leetcode.com/problems/clone-graph/
# all tests passed
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    
    copy_map = {}
    def dfs(node):

        if node in copy_map:
            return copy_map[node]

        newnode = Node(node.val)
        copy_map[node] = newnode

        for n in node.neighbors:
            newnode.neighbors.append(dfs(n))

        return newnode

    return dfs(node) if node else None
        
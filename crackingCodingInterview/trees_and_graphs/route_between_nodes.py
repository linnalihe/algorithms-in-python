# Route between nodes
# Given directed graph, find whether there is a route between two nodes

# can be solved with either breath first search or depth first search
from enum import Enum
from collections import deque


class State(Enum):
    UNVISITED = 1
    VISITED = 2
    VISITING = 3


def search(g: Graph, start: Node, end: Node):

    if(start == end):
        return True

    q = deque()
    for u in g.getNodes():
        u.state = State.UNVISITED
    start.state = State.VISITING
    q.append(start)
    while(not q.isEmpty()):
        u = q.pop()
        if(u == None):
            for v in u.getAdjacent():
                if(v.state == State.UNVISITED):
                    if(v == end):
                        return True
                    else:
                        v.state = State.VISITING
                        q.append(v)
        u.state = State.VISITED
    return False


class Graph:
    pass


class Node:
    pass

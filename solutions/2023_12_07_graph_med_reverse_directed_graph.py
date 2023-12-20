
# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-698957-1080977-56-344

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def create_transpose(node):
    """
    Args:
     node(GraphNode_int32)
    Returns:
     GraphNode_int32
    """
    # param node: node class with value and neighbors
    # return an adjacency list that has direction in reverse
    # iterate through node and neighbors with dfs
    # add pair in reverse to adj_list during dfs
    # time: iterate via dfs node and neighbors O(N+E)
    # space: visited list O(N), adj_list output O(N+E), dfs call stack O(N+C)
    
    reversed_edge_list = [None for _ in range(316)]

        
    def dfs(node):
        reversed_edge_list[node.value] = GraphNode(node.value)
        for neigh in node.neighbors:
            if reversed_edge_list[neigh.value] == None:
                dfs(neigh)
            
            
            reversed_edge_list[neigh.value].neighbors.append(reversed_edge_list[node.value])


    dfs(node)
    return reversed_edge_list[node.value]

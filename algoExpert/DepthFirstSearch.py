

# Given a Node class, implement depth-first search that takes an empty array.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

        # O(V+E) time, O(V) space
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

        # Given the Node class with a name and children nodes
        # and the nodes form an acyclic tree (there is no cycles)
        # implement dfs on Node class that takes and empty array
        # traverse through with DFS and add nodes the the array
        # return the array
        # start with self, and add to array, if there are children,
        # call dfs on the children

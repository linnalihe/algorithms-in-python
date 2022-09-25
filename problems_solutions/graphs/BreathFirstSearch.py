# Breath First Search

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        traverseQ = [self]
        while traverseQ:
            current = traverseQ.pop(0)
            # print(current.name)
            array.append(current.name)
            for child in current.children:
                traverseQ.append(child)

        return array

        # for BFS need a queue, visited, and use a while loop
        # this is acyclic os don't need a visited
        # stores nodes in input array while going through you
        # in python you can use list [] as a queue by appending to the end
        # and then pop(0) to remove from the front

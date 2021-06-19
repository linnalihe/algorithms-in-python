# Stack Min
# Design a stack that has a min function that returns the minimum element
# in addition to push and pop. push, pop, min should all be O(1)

# below is an outline of StackWithMin extending a Stack that is not implemented
# each value is a node that also stores the min value

import math


class StackWithMin(Stack):

    def push(self, value: int):
        newMin = math.min(value, min())
        super().__init__(self, NodeWithMin(value, newMin))

    def min(self):
        if(self.isEmpty()):
            raise IndexError
        else:
            return peek().min

    def peek(self):
        pass


class NodeWithMin:

    def __init__(self, v: int, min: int):
        self. value = v
        self.min = min

# another way to implement stack with min
# is to have another stack keep track of the min value
# extends Stack that holds integers rather than nodes


class StackWithMin2(Stack):

    def __init__(self):
        self.s2 = Stack()

    def push(self, value: int):
        if(value <= min()):
            self.s2.push(value)
        super().push(value)

    def pop(self):
        value = super().pop()
        if(value == min()):
            self.s2.pop()

    def min(self):
        if(self.s2.isEmpty()):
            raise IndexError
        else:
            return self.s2.peek()


class Stack:
    pass

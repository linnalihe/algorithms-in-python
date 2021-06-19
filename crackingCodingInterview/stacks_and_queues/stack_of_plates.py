# stacks of plates
# Implement data structure where when a stack exceeds a certain level, start a new stack
# push() and pop() should behave the same as if it were a single stack
# additional popAt() function to pop from a specified stack

class SetOfStacks:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []

    def getLastStack(self):
        if(self.stacks.size() == 0):
            return None
        return self.stacks.get(stacks.size() - 1)

    def push(self, v: int):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        last = getLastStack()
        return last == None or last.isEmpty()

    def popAt(self, index: int):
        return leftShift(index, True)

    def leftShift(self, index: int, removeTop: bool):
        stack = stacks[index]
        removed_item = stack.pop() if removeTop else stack.removeBottom()
        if(stack.isEmpty()):
            stacks.remove(index)
        elif(len(stacks) > index+1):
            v = leftShift(index+1, False)
            stack.push(v)

        return removed_item


class Stack:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def isFull(self): return capacity == size

    def join(self, above: Node, below: Node):
        if(below != None):
            below.above = above
        if(above != None):
            above.below = below

    def push(self, v: int):
        if(size >= capacity):
            return False
        size += 1
        n = Node(v)
        if(size == 1):
            self.bottom = n
        join(n, self.top)
        self.top = n
        return True

    def pop(self):
        t = self.top
        self.top = top.below
        self.size -= 1
        return t.value

    def isEmpty(self):
        return self.size == 0

    def removeBottom(self):
        b = self.bottom
        bottom = bottom.above
        if(self.bottom != None):
            bottom.below = None
        self.size -= 1
        return b.value


class Node:
    pass

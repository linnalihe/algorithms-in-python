# Queue via a stack
# Use two stacks to implement a queue class

class MyQueue:

    def __init__(self):
        self.stackNewest = []
        self.stackOldest = []

    def size(self):
        return len(stackNewest) + len(stackOldest)

    def add(self, value):
        stackNewest.push(value)

    def shiftStacks(self):
        if(stackOldest.isEmpty()):
            while(not stackNewest.isEmpty()):
                stackOldest.push(stackNewest.pop())

    def peek(self):
        shiftStacks()
        return stackOldest.peek()

    def remove(self):
        shiftStacks()
        return stackOldest.pop()

# Three in One
# Use a single array to implement three stacks

# can either have fixed segments or flexible/dynamic segments

class MultiStack:
    def __init__(self, stackSize: int):
        self.numOfStacks = 3
        self.stackCapacity = stackSize
        self.values = [0]*stackSize*self.numOfStacks
        self.sizes = [0]*self.numOfStacks

    # push value onto stack
    def push(self, stackNum: int,  value: int):
        # check if there is space for the next element
        if(isFull(stackNum)):
            raise IndexError
        # increment stack pointer and then update top value
        sizes[stackNum] += 1
        values[indexOfTop(stackNum)] = value

    def pop(self, stackNum: int):
        if(isEmpty(stackNum)):
            # this is probably not the right error to throw it'll have to do for now
            raise IndexError
        topIndex = indexOfTop(stackNum)
        value = values[topIndex]
        values[topIndex] = 0
        sizes[stackNum] -= 1
        return value

    def peek(self, stackNum: int):
        if(isEmpty(stackNum)):
            raise IndexError
        return values[indexOfTop(stackNum)]

    def isEmpty(self, stackNum: int):
        return sizes[stackNum] == 0

    def isFull(self, stackNum: int):
        return sizes[stackNum] == stackCapacity

    # returns the index from the top of the stack
    def indexOfTop(self, stackNum: int):
        # stackNum is the chosen stack's index
        # stackCapacity is the size of each stack
        offset = stackNum * stackCapacity
        # sizes hold how many items are in each stack
        # size will be the number of items in the chosen stack
        size = sizes[stackNum]
        return offset + size - 1


class MultiStackFlex:

    values = []
    stackInfo = []

    class StackInfo:
        def __init__(self, start: int, capacity: int):
            self.start = start
            self.capacity = capacity
            self.size = 0

        def isWithinStackCapacity(self, index: int):
            # if out of bound return false
            if(index < 0 or index >= len(values)):
                return False

        def lastCapacityIndex(self):
            return adjustIndex(self.start + self.capacity - 1)

        def lastElementIndex(self):
            return adjustIndex(self.start + self.size - 1)

        def isFull(self):
            return self.size == self.capacity

        def isEmpty(self):
            return self.size == 0

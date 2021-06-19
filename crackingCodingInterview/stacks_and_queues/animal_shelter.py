# Animal Shelter
# first in first out adoption agency
# create a data structure that implements first in first out with enqueue, dequeueAny,
# dequeueDog, and dequeueCat for dequeue-ing a specific species if that is requested

class Animal:

    order = None

    def __init__(self, name):
        self.name = name

    def setOrder(self, ord: int):
        order = ord

    def getOrder(self):
        return order

    def isOlder(self, a: Animal):
        return self.order < a.getOrder()


class AnimalQueue:

    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, a: Animal):
        a.setOrder(order)
        self.order += 1

        if(type(a) is Dog):
            dogs.push(a)
        else:
            cats.push(a)

    def dequeueDog(self):
        return dogs.pop()

    def dequeueCat(self):
        return cats.pop()

    def dequeueAny(self):
        # this chunk seems a bit off
        # what if dog is 0 and cat is 0?
        # should have a check first to throw error if both is empty
        if len(dogs) == 0:
            return dequeueCat()
        elif(len(cats) == 0):
            return dequeueDog()

        topDog = dogs[0]
        topCat = cats[0]
        if(topDog.isOlder(topCat)):
            return dequeueDog()
        else:
            return dequeueCat()


class Dog(Animal):
    def __init__(self, n):
        super(n)


class Cat(Animal):
    def __init__(self, n):
        super(n)

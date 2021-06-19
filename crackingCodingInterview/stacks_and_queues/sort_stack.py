# Sort Stack
# Write a sorted stack such that the smallest items are on top.
# You can use a temporary stack but cannot copy elements into another data structure
# should support push, pop, peek, isEmpty operations

def sort(s: list):
    r = []
    while(not s.isEmpty()):
        temp = s.pop()
        while(not r.isEmpty() and r.peek() > temp):
            s.push(r.pop())

        r.push(temp)

    while(not r.isEmpty()):
        s.push(r.pop())

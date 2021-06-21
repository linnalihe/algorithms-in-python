# Single Cycle Check

def hasSingleCycle(array):
    index = (0 + array[0]) % len(array)
    if index == 0:
        return len(array) == 1
    seen = set()
    while index != 0:
        index = (index + array[index]) % len(array)
        if index in seen:
            return False
        else:
            seen.add(index)
    return len(seen) == len(array) - 1


# input is an array = 2, 3, 1, -4, -4, 2]
# output is boolean
# function returns whether input array forms a single cycle
# every element in array is visited exactly once before landing back at
# starting index
# can use a set to keep track of indexes visited
# len of array
# start at index = 0
# next = index + array[index] % len of array, add next to set
# while next != 0 keep iterating, if there is a duplicate in the set return False

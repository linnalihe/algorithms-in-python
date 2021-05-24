# Given array of at least 3 integers, return a sorted array of 3 largest integers
# without sorting input array

# initialize with the first 3 integers
# index 0 is smallest, index 2 is largest
def findThreeLargestNumbers(array):
    output = [float('-inf'), float('-inf'), float('-inf')]
    seen = [None, None, None]
    for i in range(len(array)):
        if array[i] > output[2]:
            output[2] = array[i]
            seen[2] = i
    for j in range(len(array)):
        if array[j] > output[1] and j != seen[2]:
            output[1] = array[j]
            seen[1] = j
    for k in range(len(array)):
        if array[k] > output[0] and k != seen[1] and k != seen[2]:
            output[0] = array[k]
            seen[0] = k
    return output

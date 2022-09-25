
# O(N) for time complexity for the number of elements and the sub elements
# O(d) for space for the largest depth of the nested arrays
def productSum(array):
    depth = 1
    pSum = productSumHelp(array, depth, 0)
    return pSum


def productSumHelp(array, depth, pSum):
    tempSum = 0
    for x in array:
        if isinstance(x, int):
            tempSum += x
        else:
            tempSum += productSumHelp(x, depth+1, pSum)
    pSum += tempSum*depth

    return pSum

def maxSubsetSumNoAdjacent(array):
    if len(array) <= 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0], array[1])
    maxAtIndex = [0]*len(array)
    maxAtIndex[0] = array[0]
    maxAtIndex[1] = array[1]

    maxSubsetHelper(array, maxAtIndex)

    return maxAtIndex[len(array)-1]


def maxSubsetHelper(array, maxAtIndex):

    idx = 1
    while idx < len(array):
        maxAtIndex[idx] = max(
            maxAtIndex[idx-1], maxAtIndex[idx-2] + array[idx])
        idx += 1

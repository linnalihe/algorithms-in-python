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

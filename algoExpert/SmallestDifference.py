# Smallest Difference
# Given two non-empty arrays of integers, find pair of numbers whose absolute difference is closest to zero
# Return the pair where number from first array comes first
# Only one pair of numbers with smallest difference

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallestDiff = abs(arrayOne[0] - arrayTwo[0])
    smallestPair = [arrayOne[0], arrayTwo[0]]
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            diff = abs(arrayOne[i] - arrayTwo[j])
            if smallestDiff > diff:
                smallestDiff = diff
                smallestPair = [arrayOne[i], arrayTwo[j]]
            elif diff == 0:
                return [arrayOne[i], arrayTwo[j]]
            elif j > 0 and diff > abs(arrayOne[i] - arrayTwo[j-1]):
                break
    return smallestPair


# sort the arrays
# iterate each array and compare values
# if the difference is greater, move to next index in arrayOne
# keep track of smallest difference
# keep track of smallest difference pair
# return if difference is 0 otherwise return smallest pair

# Sorted Squared Array
# given a non-empty array of positive and negative integers sorted in ascending order,
# return a new array with integers squared also in ascending order

# O(nlogn) time for sorting, O(n) space for new array
def sortedSquaredArray(array):
    newarray = [0 for _ in array]
    for i in range(len(array)):
        newarray[i] = array[i]**2
    newarray.sort()
    return newarray

# O(n) time, O(n) space


def sortedSquaredArray2(array):

    newarray = [0 for _ in array]
    left = 0
    right = len(array)-1
    # iterating from end of list
    for i in reversed(range(len(array))):
        leftVal = array[left]
        rightVal = array[right]
        if abs(leftVal) > abs(rightVal):
            newarray[i] = leftVal*leftVal
            left += 1
        else:
            newarray[i] = rightVal*rightVal
            right -= 1
    return newarray

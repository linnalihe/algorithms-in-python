# Sorted Squared Array
# given a non-empty array of positive and negative integers sorted in ascending order,
# return a new array with integers squared also in ascending order

def sortedSquaredArray(array):
    # Write your code here.
    newarray = [0 for _ in array]
    for i in range(len(array)):
        newarray[i] = array[i]**2
    newarray.sort()
    return newarray


def sortedSquaredArray2(array):
    newarray = [0 for _ in array]
    left = 0
    right = len(array)-1
    for i in reversed(range(len(array))):
        leftVal = array[left]*array[left]
        rightVal = array[right]*array[right]
        if(rightVal <= leftVal):
            newarray[i] = leftVal
            left += 1
        else:
            newarray[i] = rightVal
            right -= 1

    return newarray


# array is sorted
# create new array of same length
# iterate through array with right and left pointer and square
# insert larger value

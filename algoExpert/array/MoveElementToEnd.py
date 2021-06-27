# Move Element to End
# Given array of integers and an integer argument called toMove,
# move all the integers in the array that is equal to the toMove
# to the end of the array, return the array

# pointer to the end of the array
# iterate array, if integer equals toMove, swap with integer at pointer
def moveElementToEnd(array, toMove):
    array.sort()
    idx = len(array)-1
    while idx >= 0 and array[idx] == toMove:
        idx -= 1

    for i in range(len(array)):
        if i < idx and array[i] == toMove:
            temp = array[idx]
            array[idx] = array[i]
            array[i] = temp
            idx -= 1
    return array

# O(n) time and O(1) space


def moveElementToEnd2(array, toMove):
    left = 0
    right = len(array) - 1
    while right > left:
        if array[left] == toMove:
            if array[right] != toMove:
                swap(left, right, array)
            else:
                right -= 1
        elif array[left] != toMove:
            if array[right] != toMove:
                left += 1
            else:
                left += 1
                right -= 1
    return array


def swap(left, right, array):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp

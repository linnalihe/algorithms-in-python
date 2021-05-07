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

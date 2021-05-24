# Given a sorted array of integers and a target integer,
# return the index of the target in the array,
# return -1 if integer not found,
# implement using binary search


#                    mid
#array [ 1, 2, 3, 4, 5, 6, 7, 8, 9], 7
def binarySearch(array, target):
    left = 0
    right = len(array)-1
    mid = int(len(array)/2)
    while left <= right:

        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            left = mid+1

        else:
            right = mid-1

        mid = int((right - left)/2)+left

    return -1

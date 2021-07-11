# Two Number Sum
# Given a non-empty array and a target with distinct integers, return an array of integer pairs that sum to the target.
# If no combination two of numbers sum to target, return an empty array

# sort the array
# have a left and right pointer
# if temp sum is less than target, move left pointer
# if temp sum is greater than target, move right pointer
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        tempSum = array[left] + array[right]
        if tempSum < targetSum:
            left += 1
        elif tempSum > targetSum:
            right -= 1
        else:
            return [array[left], array[right]]
    return []

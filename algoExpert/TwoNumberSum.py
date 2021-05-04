# Two Number Sum

# Given a non-empty array and a target with distinct integers, return an array of integer pairs that sum to the target.
# If no combination two of numbers sum to target, return an empty array

# O(n^2) time, O(1) space
def twoNumSum(array, target):
    for x in range(len(array)-1):
        for y in range(x+1, len(array)):
            if x is not y and array[x] + array[y] == target:
                return[array[x], array[y]]

    return []


# O(n) time, O(n) space
def twoNumSum2(array, target):
    matches = {}
    for n1 in array:
        n2 = target - n1
        if(n2 in matches):
            return [n1, n2]
        else:
            matches[n1] = True
    return []

# o(n log(n)) time, O(1) space


def twoNumSum3(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while right > left:
        current = array[left] + array[right]
        if(current == target):
            return [array[left], array[right]]
        elif current < target:
            left += 1
        elif current > target:
            right -= 1
    return []

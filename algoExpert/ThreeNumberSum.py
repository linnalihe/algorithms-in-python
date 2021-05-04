# Three Number Sum

# Given a non-empty array of distinct integers and a target sum, return triplets of integers that add up to target
# Numbers in the triplets should be ordered in ascending order, list of triplets should also be ordered in ascending order

# Get all the combinations for 2 numbers, then check the difference to see if there is a
# number that add up to the sum

inputArray = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

# O(N^2) time, and O(n) space


def threeNumberSum(array, target):
    array.sort()
    triplets = []
    for i in range(len(array - 2)):
        left = i+1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif(currentSum < target):
                left += 1
            elif(currentSum > target):
                right -= 1
    return triplets

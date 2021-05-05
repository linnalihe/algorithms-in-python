# Three Number Sum

# Given a non-empty array of distinct integers and a target sum, return triplets of integers that add up to target
# Numbers in the triplets should be ordered in ascending order, list of triplets should also be ordered in ascending order

# Get all the combinations for 2 numbers, then check the difference to see if there is a
# number that add up to the sum

# output array that will store all the integers that add up to targetSum
# find the difference that would add up to the targetSum
# if the sum exist, add 3 numbers to the array

def threeNumberSum(array, targetSum):
    output = []
    array.sort()
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        diff = targetSum - array[i]
        while left < right:
            tempSum = array[left] + array[right]
            if(tempSum < diff):
                left += 1
            elif(tempSum > diff):
                right -= 1
            else:
                output.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

    return output

# O(N^3 log M* log K)?


def threeNumberSum2(array, targetSum):
    output = []
    check = set()
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if(i != j and i != k and j != k and array[i]+array[j]+array[k] == targetSum):
                    tempArray = [array[i], array[j], array[k]]
                    tempArray.sort()
                    tempTup = (tempArray[0], tempArray[1], tempArray[2])
                    if(tempTup not in check):
                        output.append(tempArray)
                        check.add(tempTup)
    output.sort()
    return output

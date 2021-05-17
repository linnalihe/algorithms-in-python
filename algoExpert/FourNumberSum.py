# Given non-empty array of distinct integers, return array of unique 4 number sums
# Return empty array if no 4 number sums found

# I want to have a dictionary to keep track of 2 number sums
# I want a array to keep track of all the combinations of 4 number sums
# iterate through the array
# first inner loop check we can get to the targetsum
# second inner loop add the previous number + current number to the dicitonary

def fourNumberSum(array, targetSum):
    twopairs = {}
    quadcombo = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currSum = array[i] + array[j]
            currDiff = targetSum - currSum
            if(currDiff in twopairs):
                for pair in twopairs[currDiff]:
                    quadcombo.append(pair + [array[i]] + [array[j]])

        for k in range(0, i):
            twopairsContainer = twopairs.get(array[k]+array[i], [])
            twopairsContainer.append([array[k], array[i]])
            twopairs[array[k]+array[i]] = twopairsContainer

    return quadcombo

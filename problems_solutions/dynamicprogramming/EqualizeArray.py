# HackerRank
# Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.


# Sample Input

# STDIN       Function
# -----       --------
# 5           arr[] size n = 5
# 3 3 2 1 3   arr = [3, 3, 2, 1, 3]
# Sample Output

# 2

def equalizeArray(arr):

    #numCount = [[0 for _ in len(arr)+1] for _ in len(arr)+1]
    minEdits = float("inf")
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] != arr[j]:
                count += 1
        #print("i",arr[i], "j",arr[j], count)
        minEdits = count if count < minEdits else minEdits
    return minEdits

    # numCount = {}
    # for num in arr:
    #     numCount[num] = numCount.get(num, 0)+1

    # sortedNums = [(val, key) for key, val in numCount.items()]
    # sortedNums.sort(reverse=True)
    # edits = 0
    # for i in range(1, len(sortedNums)):
    #     count,val = sortedNums[i]
    #     edits +=count
    # return edits

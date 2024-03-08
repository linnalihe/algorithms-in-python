# https://leetcode.com/problems/maximum-subarray/
# all tests passed
def maxSubArray(nums: list[int]) -> int:
    # bruteforce is for each element, add until last index and keep largest O(n^2)
    # only add if it's positive

    maxsum = nums[0]
    currsum = 0
    for n in nums:
        if currsum < 0:
            currsum = 0
        currsum+=n
        maxsum = max(currsum, maxsum)

    return maxsum
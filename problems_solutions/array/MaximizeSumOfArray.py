# Leetcode
# Easy
# Given an array nums of integers, we must modify the array in the following way: we choose an i and replace nums[i] with -nums[i], and we repeat this process k times in total.  (We may choose the same index i multiple times.)

# Return the largest possible sum of the array after modifying it in this way.


# Example 1:

# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose indices (1,) and nums becomes [4,-2,3].
# Example 2:

# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
# Example 3:

# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

# You want to flip the sign of the smallest value of the array k times

# Your runtime beats 46.02 % of python3 submissions.

from heapq import heapify, heappop, heappush


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        heapify(nums)

        for i in range(k):

            smallest = -heappop(nums)
            heappush(nums, smallest)

        return sum(nums)

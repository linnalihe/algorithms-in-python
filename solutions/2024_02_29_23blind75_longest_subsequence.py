# https://leetcode.com/problems/longest-increasing-subsequence/
# all tests passed
def lengthOfLIS(nums: list[int]) -> int:
    # we can either choose to include or exclude the number
    # start with idx == len(nums) because that is when
    # longest is 1
    # then moving backwards in the nums array, choose max of curr dp or prev dp +1
    if not nums:
        return 0
    nums_dp = [1]*len(nums)

    for i_idx in reversed(range(len(nums))):
        for j_idx in range(i_idx+1, len(nums)):
            if nums[i_idx] < nums[j_idx]:
                nums_dp[i_idx] = max(nums_dp[i_idx], 1+nums_dp[j_idx])

    return max(nums_dp)
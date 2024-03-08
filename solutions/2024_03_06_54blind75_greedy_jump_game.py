# https://leetcode.com/problems/jump-game/
# all tests passed
def canJump(nums: list[int]) -> bool:
    # bruteforce is to try all combinations until you get to the end
    # try the max jump and decrement from there if we hit a zero
    # want to get to idx == len(nums)-1

    end = len(nums) - 1
    for idx in reversed(range(len(nums))):
        if idx+nums[idx] >= end:
            end = idx

    return True if end == 0 else False
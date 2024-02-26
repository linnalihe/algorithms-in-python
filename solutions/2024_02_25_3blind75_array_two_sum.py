# https://leetcode.com/problems/two-sum/
# all tests passed
def twoSum(nums: list[int], target: int) -> list[int]:

        diff_map = {}
    
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in diff_map:
                return [idx, diff_map[diff]]

            diff_map[val] = idx
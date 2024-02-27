# https://leetcode.com/problems/house-robber/
# all tests passed
def rob(nums: list[int]) -> int:
        
        choice1 = 0
        choice2 = 0

        for num in nums:
            max_robbed = max(num+choice1, choice2)
            choice1 = choice2
            choice2 = max_robbed


        return max(choice1, choice2)
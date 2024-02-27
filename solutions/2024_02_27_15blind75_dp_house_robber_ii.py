# https://leetcode.com/problems/house-robber-ii/
# all tests passed 
def rob(nums: list[int]) -> int:

    def helper(subnums):

        choice1 = 0
        choice2 = 0

        for num in subnums:
            max_result = max(num+choice1, choice2)
            choice1 = choice2
            choice2 = max_result

        return max(choice1, choice2)
    

    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
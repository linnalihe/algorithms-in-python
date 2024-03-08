
# https://leetcode.com/problems/missing-number/
# all tests passing
def missingNumber(nums: list[int]) -> int:

    output = 0
    for i in range(len(nums)+1):
        output ^= i

    for n in nums:
        output^=n

    return output
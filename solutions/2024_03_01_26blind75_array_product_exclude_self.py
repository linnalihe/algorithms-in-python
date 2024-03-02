# https://leetcode.com/problems/product-of-array-except-self/
# all tests passed
def productExceptSelf(nums: list[int]) -> list[int]:
    # brute force is for each element, look through all elements
    # and skip the current idx on the 2nd for loop to add up all values
    # O(n^2) time and O(n) space for output
    # better to initialize an output the all values == 1
    # can run a for loops but not nexted and exlcude the idx

    res = [1]*len(nums)

    curr_product = 1
    for idx in range(len(nums)):
        res[idx] *= curr_product
        curr_product*=nums[idx]
    
    curr_product = 1
    for idx in reversed(range(len(nums))):
        res[idx] *= curr_product
        curr_product *= nums[idx]

    return res
# https://leetcode.com/problems/maximum-product-subarray/description/
# all tests passed
def maxProduct(nums: list[int]) -> int:
    # bruteforce generate all subarrays and and keep track of the largest
    # at each step, keep track of min and max of the products with dp

    output = max(nums)
    minval = 1
    maxval = 1

    for n in nums:
        if n == 0:
            minval = 1
            maxval = 1
            continue 

        prevmin = minval
        minval = min(maxval*n, minval*n, n)
        maxval = max(maxval*n, prevmin*n, n)
        output = max(output, maxval)
    return output
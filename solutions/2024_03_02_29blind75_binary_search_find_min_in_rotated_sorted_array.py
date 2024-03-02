# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# all tests passed
def findMin(nums: list[int]) -> int:
    # must use binary search to achieve O(log n)
    # if val is less then right and left, it's the minimum
    # if it's not, using [4,5,6,7,0,1,2], mid is 7 we want to look at right
    # because mid+1 and end is less than start and mid-1
    # using [0,1,2,4,5,6,7] as example, 4 we want left bc start<mid+1, mid-1<end
    res = nums[0]
    start = 0
    end = len(nums)-1
    if nums[start] < nums[end]:
        return res
    
    while start <= end:
        mid = (start+end)//2
        
        res = min(res, nums[mid])
        if nums[start] <= nums[mid] and nums[end] <= nums[start]:
            start = mid+1
        else:
            end=mid-1
    return res
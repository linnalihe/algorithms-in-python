# https://leetcode.com/problems/sort-an-array/description/
# all tests passed

import random
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        self.merge_sort_helper(nums, 0, len(nums)-1)
        return nums


    def merge_sort_helper(self, nums, start, end):
        if start >= end:
            return

        mid = (start + end) //2

        self.merge_sort_helper(nums, start, mid)
        self.merge_sort_helper(nums, mid+1, end)

        temp = []
        left = start
        right = mid+1

        while left <= mid and right <=end:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1

        while left <= mid:
            temp.append(nums[left])
            left+=1

        while right <= end:
            temp.append(nums[right])
            right+=1

        idx = start
        for val in temp:
            nums[idx] = val
            idx+=1
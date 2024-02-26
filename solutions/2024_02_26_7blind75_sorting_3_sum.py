# https://leetcode.com/problems/3sum/
# all tests passed
def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = set()
        for idx in range(len(nums)):
            left = idx+1
            right = len(nums)-1
            while left < right:
                three_sum = nums[idx] + nums[left] + nums[right]
                if three_sum < 0:
                    left+=1
                elif three_sum > 0:
                    right-=1
                else:
                    t = (nums[idx], nums[left], nums[right])
                    if not t in output:
                        output.add((nums[idx], nums[left], nums[right]))

                    left+=1
                    right-=1

        return output
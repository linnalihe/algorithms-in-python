# https://leetcode.com/problems/container-with-most-water/description/
# all tests passed
def maxArea(height: list[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) -1
        while left < right:
            currarea = min(height[left], height[right])*(right-left)
            maxarea = max(maxarea, currarea)

            if height[right] > height[left]:
                left+=1
            else:
                right-=1

        return maxarea
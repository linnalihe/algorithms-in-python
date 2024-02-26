# https://leetcode.com/problems/contains-duplicate/description/
# passed all tests
def containsDuplicate(nums: list[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:
                return True
            seen.add(val)

        return False
# https://leetcode.com/problems/longest-consecutive-sequence/
# all tests passed
def longestConsecutive(nums: list[int]) -> int:
    # brute force is for each element, start counting
    # time is O(n^2)
    # better to use and array to store the values and count the index
    if not nums:
        return 0

    longest = 0
    num_bank = set()

    for n in nums:
        num_bank.add(n)
    
    for n in nums:
        # if there is no previous value, then it's the start 
        # of a new sequence
        if n-1 not in num_bank:
            temp = 0
            while n+temp in num_bank:
                temp+=1

            longest = max(longest, temp)

    return longest
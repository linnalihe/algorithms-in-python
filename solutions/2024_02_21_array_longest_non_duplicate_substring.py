# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# all tests passed
def lengthOfLongestSubstring(s: str) -> int:
        # brute force is to look at every substring and keep
        # track of the longest. time is O(n^2), space is O(1), just a variable to keep track of longest
        # better is sliding window to look at all chars in the 
        # string once and exclude them on the left as we see duplicates
        # time is O(n), space is O(n) to keep track of seen chars
        longest = 0
        in_view = set()

        left = 0
        right = 0
        # use a sliding window to exclude duplicates on
        # the left as we move the right pointer forward
        while right < len(s):
            while s[right] in in_view:
                # as long as we see value at idx right we keep
                # removing left values until we have removed
                # the duplicate
                in_view.remove(s[left])
                left+=1

            # then add the right value once there isn't
            # a duplicate on the left
            in_view.add(s[right])
            
            # check if this non-duplicate string is
            # longer than the longest string
            if longest < right-left+1:
                longest = right-left+1
            right +=1
                

        return longest
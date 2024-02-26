# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# all tests passed
def lengthOfLongestSubstring(s: str) -> int:
        # bruteforce is to compare all O(n^2)
        # keep track of the longest seen and take away from left if duplicate
        # time O(n) to do one pass of str
        # space is O(1)
        max_substring = 0
        view = set() # we only accomodate at most 1 duplicate so we can use a set
        left=0
        right=0
        while right < len(s):
            
            if s[right] in view:
                # keep moving left forward until duplicate removed
                while s[right] in view:
                    view.remove(s[left])
                    left+=1
            
            max_substring = max(max_substring, right-left+1)
            view.add(s[right])
            right+=1
            
        
        return max_substring
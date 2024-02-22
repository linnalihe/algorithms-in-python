# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/submissions/1182489185/
# passed all tests

from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # bruteforce is to look at all substrings O(n^2)
        # compare with dictionary to check if it's valid and store the max O(n)
        # total time is O(n^3)

        # make a dictionary of the frequency of each character
        # if the frequency is less than k, find the longest 
        # substring excluding that character

        if len(s) < k:
            return 0

        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] +=1

        for char, value in freq_map.items():
            if value < k:
                return max(self.longestSubstring(substring, k) for substring in s.split(char))
        
        return len(s)
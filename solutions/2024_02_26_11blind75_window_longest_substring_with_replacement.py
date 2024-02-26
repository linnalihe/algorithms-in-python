# https://leetcode.com/problems/longest-repeating-character-replacement/
# all tests passed
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # bruteforce at each index replace k times with letter at idx, O(n^2)
        # expand window from index as long as letter is same
        # better to create dictionary and look at most freqent
        # for each idx, look up freq and then count number of differing char
        # until idx with same. diff is the chars need to be replaced
        longest = 0
        letter_map = defaultdict(int)

        left = 0
        right = 0
        while right < len(s):
            letter_map[s[right]] +=1

            max_freq = self.get_max_freq(letter_map)
            diff = (right-left+1) - max_freq
            if diff > k:
                letter_map[s[left]] -=1
                left+=1
            else:
                longest = max(right-left+1, longest)
            
            right+=1
            
        return longest


    def get_max_freq(self, letter_map):
        mfreq = 0
        for val in letter_map.values():
            mfreq = max(val, mfreq)

        return mfreq
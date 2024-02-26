# https://leetcode.com/problems/valid-anagram/
# all tests passed
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
        
        letter_freq = defaultdict(int)
        for l in s:
            letter_freq[l] +=1

        for l in t:
            letter_freq[l] -=1

        for val in letter_freq.values():
            if val != 0:
                return False

        return True
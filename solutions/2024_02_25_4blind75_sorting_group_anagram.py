# https://leetcode.com/problems/group-anagrams/
# all tests passed
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    anagram_map = defaultdict(list)
    for val in strs:
        val_key = "".join(sorted(val))
        anagram_map[val_key].append(val)

    return [val for val in anagram_map.values()]
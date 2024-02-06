# https://leetcode.com/problems/first-unique-character-in-a-string/
# all tests passed

from collections import defaultdict

def firstUniqChar(self, s: str) -> int:
        # brute force where you look at a char and check
        # subsequent char will be n^2
        # use a dictionary to keep track
        # time: O(n)
        # space: O(n)

        output = -1
        seen = defaultdict(int)
        for char in s:
            seen[char] += 1

        for idx, char in enumerate(s):
            if seen[char] == 1:
                output = idx
                break

        return output

# Sample tests
# "leetcode"
# "loveleetcode"
# "aabb"
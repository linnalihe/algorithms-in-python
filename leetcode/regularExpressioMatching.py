# Hard
# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).


# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input: s = "aab", p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input: s = "mississippi", p = "mis*is*p*."
# Output: false


# Constraints:

# 0 <= s.length <= 20
# 0 <= p.length <= 30
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

# Testcase:
# "aa"
# "a"
# "aa"
# "a*"
# "ab"
# ".*"
# "aab"
# "c*a*b"
# "mississippi"
# "mis*is*p*."
# "ab"
# ".*c"
# "aaa"
# "a*a"
# "aaa"
# "aaaa"
# "a"
# "ab*a"

# explanation: https://www.techiedelight.com/wildcard-pattern-matching/


# case 1 : string has to match completely
# case 2 : support of "." so that "." replaces any single character
# case 3 : support of "*" so that zero or more of preceeding character
# when you get a "*" you corresponding sIndex value needs to be equal to pIndex-1 value, if not equal, increment

# iterate through p and check if the value is in s
# use pointer move through both


# my incomplete implementation, this solutions does not work:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sIndex = 0
        pIndex = 0
        while sIndex < len(s) and pIndex < len(p):
            if(pIndex+1 < len(p) and p[pIndex+1] == "*"):

                while sIndex < len(s) and (s[sIndex] == p[pIndex] or p[pIndex] == "."):
                    sIndex += 1
                pIndex += 2
            elif(p[pIndex] == s[sIndex] or p[pIndex] == "."):
                pIndex += 1
                sIndex += 1
            else:
                break
        # pIndex can be ".", "*", or a lowercase letter
        # pIndex val has to be equal to the last

        remainMatch = (p[len(p)-1] == s[sIndex-1]
                       ) or (p[len(p)-1] == ".") or (p[len(p)-1] == "*")
        if("*" not in p):
            return len(s) == sIndex and len(p) == pIndex
        return len(s) == sIndex and remainMatch


# leetcode recursive solution
class Solution:
    def isMatch2(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], "."}
        if len(pattern) >= 2 and pattern[1] == "*":
            return self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

# leetcode dynamic programming solution


class Solution(object):
    def isMatch3(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {
                        text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

# leetcode bottom up solution


class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

# https://leetcode.com/problems/palindromic-substrings/submissions/1188170296/
# all tests passed
def countSubstrings(s: str) -> int:

    num_palin_substrs = 0

    for idx in range(len(s)):

        left = idx
        right = idx
        while left >= 0 and right <len(s) and s[right] == s[left]:
            num_palin_substrs +=1
            left-=1
            right+=1

        left = idx
        right = idx +1
        while left >= 0 and right <len(s) and s[right] == s[left]:
            num_palin_substrs +=1
            left-=1
            right+=1

    return num_palin_substrs
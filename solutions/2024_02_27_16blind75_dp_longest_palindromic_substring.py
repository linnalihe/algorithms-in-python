
# https://leetcode.com/problems/longest-palindromic-substring/
# all tests passed
def longestPalindrome(s: str) -> str:
    longest_substring = ""
    longest_count = 0

    for idx in range(len(s)):
        left = idx
        right = idx
        while left >=0 and right < len(s) and s[left] == s[right]:
            count = right-left+1
            if count > longest_count:
                longest_count = count
                longest_substring = s[left:right+1]
            left-=1
            right+=1
        
        left=idx
        right=idx+1
        while left >=0 and right < len(s) and s[left] == s[right]:
            count = right - left +1
            if count > longest_count:
                longest_count = count
                longest_substring = s[left:right+1]
            left-=1
            right+=1
    
    return longest_substring
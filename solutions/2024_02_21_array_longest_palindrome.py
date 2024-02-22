# https://leetcode.com/problems/longest-palindromic-substring/submissions/1182527937/
# all tests passed

def longestPalindrome(s: str) -> str:
        # bruteforce is to look at all substring and keep track of longest
        # at each substring, check if it's a palindrome O(n)
        # O(n^3) time and O(n) space where n is length of s
        # check s is palindrome incrementally by expanding outwards
        
        longest = ""

        for idx in range(len(s)):
            left = idx
            right = idx
            while left >= 0 and right <len(s) and s[left] == s[right]:
                if len(longest) < len(s[left:right+1]):
                    longest = s[left:right+1]
                left-=1
                right+=1

            left = idx
            right = idx+1
            while left >= 0 and right <len(s) and s[left] == s[right]:
                if len(longest) < len(s[left:right+1]):
                    longest = s[left:right+1]
                left-=1
                right+=1

        return longest
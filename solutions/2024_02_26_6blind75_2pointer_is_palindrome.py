def isPalindrome(s: str) -> bool:
        keep_set = "abcdefghijklmnopqrstuvwxyz0123456789"
        s_v2 = []
        for letter in s.lower():
            if letter in keep_set:
                s_v2.append(letter)

        left = 0
        right = len(s_v2) -1
        while left<right:
            if s_v2[left] != s_v2[right]:
                return False
            left+=1
            right-=1

        return True
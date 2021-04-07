class Solution:
    
    
    def longestPalindrome(self, s: str) -> str:
        
        def isPalinDrome( s: str) -> bool:
            isPalin = True;
            for i in range(int(len(s)/2+1)):
                if(s[i] is not s[len(s)-1-i]):
                    isPalin = False;
                    break;
                
            return isPalin
        
        longestStr = ""
        strCount = 0
        
        for i in range(len(s)):
            if(strCount > len(s[i:])):
                break;
            for j in range(len(s), i, -1):   
          
                if isPalinDrome(s[i:j+1]) and len(s[i:j+1]) > strCount:
                    longestStr = s[i:j+1]
                    strCount = len(s[i:j+1])
                    break;
            
            
                    
        return longestStr
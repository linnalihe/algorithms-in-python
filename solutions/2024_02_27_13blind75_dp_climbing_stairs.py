# https://leetcode.com/problems/climbing-stairs/submissions/1187946957/
# all tests passed
def climbStairs(n: int) -> int:
        v1 = 1
        v2 = 1

        for idx in range(n-1):
            temp = v1
            v1 = v1 + v2
            v2 = temp
        
        return v1
# https://leetcode.com/problems/climbing-stairs/
def climbStairs(n: int) -> int:
        memo = {}
        
        def find_n(n, memo):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1

            memo[n] = climbStairs(n-1) + climbStairs(n-2)
            
            return memo[n]
        
        return find_n(n, memo)
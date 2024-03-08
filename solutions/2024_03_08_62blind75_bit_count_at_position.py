# https://leetcode.com/problems/counting-bits/description/
# all tests passed
def countBits(n: int) -> list[int]:
        dp = [0] * (n+1)

        cp = 1
        for idx in range(1, n+1):
            if idx == cp * 2:
                cp = idx

            dp[idx] = dp[idx-cp] +1

        return dp
# https://leetcode.com/problems/unique-paths/
# all tests passed
def uniquePaths(m: int, n: int) -> int:
    # brute force is do a dfs and cache the values that overlap
    # dp solution is to create a (n+1) * (m+1) grid and count backwards
    # from the finish
    row = m
    col = n

    count_dp = [[1]*(col) for _ in range(row)]

    for row in reversed(range(m-1)):
        for col in reversed(range(n-1)):
            count_dp[row][col] = max(
                count_dp[row+1][col]+1, 
                count_dp[row][col+1]+1, 
                count_dp[row+1][col] + count_dp[row][col+1])

    return count_dp[0][0]
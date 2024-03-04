# https://leetcode.com/problems/number-of-islands/
# all tests passed
def numIslands(grid: list[list[str]]) -> int:
    # for each cell, do a dfs if neighbor is unvisited
    # time O(m*n), space is O(1)

    count = 0
    row_len = len(grid)
    col_len = len(grid[0])

    def dfs(row, col):

        if row >= row_len or row < 0 or col >= col_len or col < 0 or grid[row][col] != "1":
            return
        
        grid[row][col] = "0"
        for nrow, ncol in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            dfs(nrow, ncol)


    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == "1":
                count+=1
                dfs(row, col)

    return count
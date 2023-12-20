# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1590
# passed tests
# space: O(1), only using var to store output which is a single int
# time: O(N) for row*col
# iterate and use dfs, use a list to pass through dfs to count size of island
def max_island_size(grid):
    """
    Args:
     grid(list_list_int32)
    Returns:
     int32
    """
    # param grid: list of list of ints 1s and 0s
    # find the largest group of 1s
    # loop through grid and if cell is 1, dfs to count island size
    # return the max of island sizes
    
    largest_size = 0
    
    def get_neighbors(row, col):
        
        res = []
        
        for nrow, ncol in (
            (row, col-1), (row, col+1), 
            (row+1, col), (row-1, col)):
            if nrow >= 0 and nrow < len(grid) and ncol >=0 and ncol < len(grid[0]):
                res.append((nrow, ncol))
                
        return res
    
    def dfs_count_island(row, col, count):
        
        grid[row][col] = 0
        count[0] +=1
        for nrow, ncol in get_neighbors(row, col):
            if grid[nrow][ncol] == 1:
                
                dfs_count_island(nrow, ncol, count)
            
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count = [0]
                dfs_count_island(row, col, count)
                largest_size = max(largest_size, count[0])
    return largest_size
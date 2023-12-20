# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1589
# pass tests
# space: O(1) - doesn't use extra space
# time: O(N) - N is the number of rows * cols
# iterate once, dfs, check cell is 1 during dfs, change val to 0 instead of storing in visited
def count_islands(matrix):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # param matrix is list of list of ints, only 1s and 0s
    # loop thru and only look at if it's a 1
    # change 1 to 0 if visited
    # use dfs on neighbors
    
    num_islands = 0
    
    
    def get_neighbors(row, col):
        
        neighbors = []
        
        for nrow, ncol in ((row, col+1), (row, col-1), (row+1, col+1), (row+1, col), (row+1, col-1),
        (row-1, col+1), (row-1, col), (row-1, col-1)):
            if nrow >=0 and nrow < len(matrix) and ncol >=0 and ncol < len(matrix[0]):
                neighbors.append((nrow, ncol))
                
        return neighbors
    
    def dfs(row, col):
        
        matrix[row][col] = 0
        for nrow, ncol in get_neighbors(row, col):
            if matrix[nrow][ncol] == 1:
                dfs(nrow, ncol)
    
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                num_islands +=1
                dfs(row, col)

    return num_islands
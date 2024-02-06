# https://leetcode.com/problems/word-search/
# passed tests on leetcode

def exist(board: list[list[str]], word: str) -> bool:
        # it's a search problem that can be solved with traversing board
        # dfs or bfs

        # param board is list of list of string that form a matrix
        # word is string that we want to find
        # going with dfs
        # time: O(n+e), space: O(n+e) => lets discuss in feedback

        # assume that it's case sentive so we are not modifying when comparing

        # feedback -> got into complexity too early. comparing dfs vs bfs unnecessary
        # analyzing complexity was not good

        m = len(board)
        n = len(board[0])
        

        def dfs_find_next(row, col, k):
            # curr_val stores the concatenated string up to this point

            if k == len(word):
                return True

            if row < 0 or row >=m or col <0 or col >=n or board[row][col] != word[k]:
                return False

            

            # get the next neighbors or the current cell
            # do another dfs to get the next word
            # get_neightbor should return list of up, down, left, right that is within
            # the bound of the board
            temp = board[row][col]
            board[row][col] = "."
            for nrow, ncol in ((row+1, col), (row-1, col), (row, col-1), (row, col+1)):
                
                if dfs_find_next(nrow, ncol, k+1):
                    return True
                
            board[row][col] = temp

            return False

            

        for row in range(m):
            for col in range(n):
                # for each cell, do a dfs and if that path finds the solution
                # we can return True
                if word[0] == board[row][col]:
                    if dfs_find_next(row, col, 0):
                        return True

        return False


# Sample test cases
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCCED"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "SEE"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"
# [["a","b"],["c","d"]]
# "cdba"
# [["a"]]
# "a"
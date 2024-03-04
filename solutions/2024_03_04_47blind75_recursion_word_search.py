# https://leetcode.com/problems/word-search/
# all tests passed 
def exist(board: list[list[str]], word: str) -> bool:
        
    row_len = len(board)
    col_len = len(board[0])

    def dfs(rowidx, colidx, k):

        if k == len(word):
            return True
        
        if rowidx >= row_len or rowidx <0 or colidx >= col_len or colidx < 0 or word[k] != board[rowidx][colidx]:
            return False

        temp = board[rowidx][colidx]
        board[rowidx][colidx] = "_"
        
        for nrowidx, ncolidx in [(rowidx+1, colidx), (rowidx-1, colidx), (rowidx, colidx+1), (rowidx, colidx-1)]:
            if dfs(nrowidx, ncolidx, k+1):
                return True
            
        board[rowidx][colidx] = temp
        
        return False


    for rowidx in range(row_len):
        for colidx in range(col_len):

            if word[0] == board[rowidx][colidx]:
                if dfs(rowidx, colidx, 0):
                    return True

    return False


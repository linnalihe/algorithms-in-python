# https://leetcode.com/problems/pacific-atlantic-water-flow/
# all tests passed
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    # find a path to an edge that is row == 0 or col == 0 AND row == len(heights)-1 or col = len(heights)-1
    # top right and bottom left already touch pacific and atlantic
    # bruteforce is for each cell, traverse entire graph and keep track of
    # touching atlantic and pacific or adjacent cell meets these conditions


    output = set()
    row_len = len(heights)
    col_len = len(heights[0])

    def touch_pacific(rowidx, colidx):
        return rowidx == 0 or colidx == 0
    
    def touch_atlantic(rowidx, colidx):
        return rowidx == len(heights)-1 or colidx == len(heights[0])-1

    def can_bridge(rowidx, colidx, status, start):

        status[0] = status[0] or touch_pacific(rowidx, colidx)
        status[1] = status[1] or touch_atlantic(rowidx, colidx)

        if (status[0] and status[1]):
            output.add(start)
            return 

        temp = heights[rowidx][colidx]
        heights[rowidx][colidx] = -1
        for nrowidx, ncolidx in ((rowidx+1, colidx), (rowidx-1, colidx), (rowidx, colidx+1), (rowidx, colidx-1)):

            if (nrowidx >= 0 and 
            nrowidx < row_len and 
            ncolidx >= 0 and 
            ncolidx < col_len and 
            heights[nrowidx][ncolidx] > -1
            and heights[nrowidx][ncolidx] <= temp
            ):
                
                can_bridge(nrowidx, ncolidx, status, start)

        heights[rowidx][colidx] = temp


    for rowidx in range(row_len):
        for colidx in range(col_len):
            can_bridge(rowidx, colidx, [False, False], (rowidx, colidx))
                
    return output
# https://leetcode.com/problems/set-matrix-zeroes/
# all tests passed
def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    toprow = [matrix[i][0] for i in range(len(matrix))]
    topcol = [val for val in matrix[0]]

    for rowidx in range(len(matrix)):
        for colidx in range(len(matrix[0])):
            if matrix[rowidx][colidx] == 0:
                toprow[rowidx] = 0
                topcol[colidx] = 0

    for rowidx in range(len(matrix)):
        for colidx in range(len(matrix[0])):
            if toprow[rowidx] == 0 or topcol[colidx] == 0:
                matrix[rowidx][colidx] = 0
    
    return matrix
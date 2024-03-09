# https://leetcode.com/problems/rotate-image/
# all tests passed
def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    left = 0
    right = len(matrix)-1

    while left < right:

        for idx in range(right - left):

            up = left
            down = right

            temp = matrix[up][left+idx]

            matrix[up][left+idx] = matrix[down-idx][left]

            matrix[down-idx][left] = matrix[down][right-idx]

            matrix[down][right-idx] = matrix[up+idx][right]

            matrix[up+idx][right] = temp

        left+=1
        right-=1
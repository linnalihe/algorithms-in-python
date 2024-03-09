# https://leetcode.com/problems/spiral-matrix/
# all tests passed
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    # first row, last col, last row, first col
    # decrement row and col
    output = []
    left = 0
    right = len(matrix[0])-1

    top = 0
    bottom = len(matrix)-1

    while left <= right and top <=bottom:
        for idx in range(left, right+1):
            output.append(matrix[top][idx])
        top +=1
        for idx in range(top, bottom+1):
            output.append(matrix[idx][right])
        right-=1

        if left > right or top > bottom:
            break

        for idx in reversed(range(left, right+1)):
            output.append(matrix[bottom][idx])
        bottom-=1
        for idx in reversed(range(top, bottom+1)):

            output.append(matrix[idx][left])
        left +=1


    return output    
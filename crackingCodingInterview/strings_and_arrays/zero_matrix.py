# Write an algorithm such that if an element in an
# MxN matrix is 0, its entire row and column are set to 0

# if there is a 0, entire row and entire column is 0
# 1st pass: as you go through note which row and columns are 0
# 2nd pass: make these rows and columns 0

def zero_matrix(matrix: list):
    columns = dict()
    rows = dict()
    colLen = len(matrix)
    rowLen = len(matrix[0])
    for i in range(colLen):
        for j in range(rowLen):
            if matrix[i][j] == 0:
                columns[i] = True
                rows[j] = True

    for i in range(colLen):
        for j in range(rowLen):
            if columns.get(i, False) or rows.get(j, False):
                matrix[i][j] = 0

    return matrix


def sol_zero_matrix(matrix: list):
    row = [False]*len(matrix)
    column = [False]*len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                row[i] = True
                column[j] = True

    # Nullify cols
    for j in range(len(matrix[0])):
        if(column[j]):
            nullifyColumn(matrix, j)

    # Nullify rows
    for i in range(len(matrix)):
        if(row[i]):
            nullifyRow(matrix, i)

    return matrix


def nullifyColumn(matrix, col):
    for j in range(len(matrix)):
        matrix[j][col] = 0


def nullifyRow(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def sol2_set_zeros(matrix):
    rowHasZero = False
    colhasZero = False

    for j in range(len(matrix[0])):
        if(matrix[0][j] == 0):
            rowHasZero = True
            break
    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            colHasZero = True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if(matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)):
        if(matrix[i][0] == 0):
            nullifyRow(matrix, i)
    for j in range(len(matrix[0])):
        if(matrix[0][j] == 0):
            nullifyColumn(matrix, j)

    if(rowHasZero):
        nullifyRow(matrix, 0)

    if(colHasZero):
        nullifyColumn(matrix, 0)

    return matrix


if __name__ == "__main__":
    matrix = [[1, 0, 5, 0, 8], [4, 1, 3, 5, 7], [0, 1, 2, 3, 4]]
    matrix2 = [[1, 0, 5, 0, 8], [4, 1, 3, 5, 7], [0, 1, 2, 3, 4]]
    matrix3 = [[1, 0, 5, 0, 8], [4, 1, 3, 5, 7], [0, 1, 2, 3, 4]]

    print(zero_matrix(matrix))
    print(sol_zero_matrix(matrix2))
    print(sol_zero_matrix(matrix3))

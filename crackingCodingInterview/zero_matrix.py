# Write an algorithm such that if an element in an
# MxN matrix is 0, its entire row and column are set to 0

# if there is a 0, entire row and entire column is 0
# 1st pass: as you go throug note which row and columns are 0
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


if __name__ == "__main__":
    matrix = [[1, 0, 5, 0, 8], [4, 1, 3, 5, 7], [0, 1, 2, 3, 4]]
    print(zero_matrix(matrix))

# Q1.7 of Cracking the Coding Interview 6
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. (an you do this in place?


def rotate_matrix(matrix: list):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return matrix
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for id_x in range(n):
        for id_y in range(n):
            new_x = id_y
            new_y = n-1-id_x

            # print("new_y", new_y)
            # print(id_y)
            # print("new_x", new_x)
            # print("new_y", new_y)
            # print(matrix[new_x][new_y])
            # print(new_matrix[id_x][id_y])
            new_matrix[new_x][new_y] = matrix[id_x][id_y]

    return new_matrix


def sol_rotate_matrix(matrix: list):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return matrix
    n = len(matrix)
    for layer in range(int(n/2)):

        first = layer
        last = n-1-layer

        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix1))
    print(sol_rotate_matrix(matrix2))

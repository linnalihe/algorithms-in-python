# get all of the first array
# get the last of the len matrix
# get the last array
# get the first of the len of matrix

# array_index =[
# 	[00, 01, 02, 03],
# 	[10, 11, 12, 13],
# 	[20, 21, 22, 23],
# 	[30, 31, 32, 33] <- last on is `len(matrix)len(array)`
# ]

# len of matrix = M
# len of array = N
# iterate through first array 00 to 0N
# iterate through len of matrix 1N to MN
# iterate through last array backwards M(N-1) to M0
# iterate through M0 to 10

# m_index and n_index
# mn_items = len(matrix)*len(matrix[0]), while count < mn_items
# continue to increment / decrement m_index and n_index to follow
# iteration pattern from above

# follow is not complete:

def spiralTraverse(array):
    m_len = len(array)
    n_len = len(array[0])
    mn_items = m_len*n_len
    output = [0]*mn_items
    m_index = 0
    n_index = 0
    counter = 0
    while counter < mn_items:
        break

        print(mn_items)
    return output

# https://leetcode.com/problems/longest-common-subsequence/
# passed all tests
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # build a 2d matrix that is len(text1)+1 x len(text2)+1
    # if the char is equal add from diagonal
    # if not equal, get max of left and right
    col = len(text1)
    row = len(text2)

    dp_matrix = [[1]*(col+1) for _ in range(row+1)]
    for idx in range(col+1):
        dp_matrix[row][idx] = 0

    for idx in range(row+1):
        dp_matrix[idx][col] = 0

    for i in reversed(range(row)):
        for j in reversed(range(col)):
            if text1[j] == text2[i]:
                dp_matrix[i][j] = dp_matrix[i+1][j+1] +1
            else:
                dp_matrix[i][j] = max(dp_matrix[i][j+1], dp_matrix[i+1][j])
    
    return dp_matrix[0][0]
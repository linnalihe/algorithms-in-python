# https://leetcode.com/problems/reverse-bits/
# all tests passed
def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):

        res = res | (((n >> i) & 1) << (31-i))

    return res
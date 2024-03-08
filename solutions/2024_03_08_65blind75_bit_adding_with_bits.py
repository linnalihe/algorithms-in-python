# https://leetcode.com/problems/sum-of-two-integers/
# all tests passed
def getSum(a: int, b: int) -> int:

    carry = 0
    mask = 0xffffffff

    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a&mask if b > mask else a
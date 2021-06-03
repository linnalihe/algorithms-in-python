# Easy
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"


# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

# Runtime: 72 ms, faster than 7.41% of Python3 online submissions for Add Strings.
# Memory Usage: 14.5 MB, less than 18.19% of Python3 online submissions for Add Strings.

# I had some difficulties with this.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        p1 = len(num1)-1
        p2 = len(num2)-1

        sum1 = []
        remain = 0
        while p1 >= 0 or p2 >= 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            sum1.append((x1 + x2 + remain) % 10)
            remain = (x1 + x2 + remain)//10
            p1 -= 1
            p2 -= 1

        if remain:
            sum1.append(remain)

        return "".join(str(x) for x in sum1[::-1])

# Runtime: 60 ms, faster than 10.81% of Python3 online submissions for Add Strings.
# Memory Usage: 14.7 MB, less than 9.55% of Python3 online submissions for Add Strings.


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:

        p1 = len(num1)-1
        p2 = len(num2)-1

        sum1 = ["0"]*(p1+1) if p1 > p2 else ["0"]*(p2+1)
        s1 = len(sum1)-1
        remain = 0
        while p1 >= 0 or p2 >= 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            sum1[s1] = ((x1 + x2 + remain) % 10)
            remain = (x1 + x2 + remain)//10
            p1 -= 1
            p2 -= 1
            s1 -= 1

        if remain:
            sum1 = [remain] + sum1

        return "".join(str(x) for x in sum1)

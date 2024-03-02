
# https://www.lintcode.com/problem/659/
# passed all tests
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        output = []
        for idx in range(len(strs)):
            word_count = len(strs[idx])
            output.append(f"{word_count}%{strs[idx]}")

        return "".join(output)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        if str == "":
            return ""

        output = []
        i = 0
        while i < len(str):
            j = i
            while j < len(str) and str[j] != "%":
                j+=1

            word_count = int(str[i:j])
            output.append(str[j+1:j+1+word_count])

            i=j+1+word_count

        return output
# https://leetcode.com/problems/decode-ways/
# all tests passed
def numDecodings(s: str) -> int:
        # return the count of the different ways to decode
        # 1 to 26
        # brute force is to generate all subsets and add count if
        # the num maps to valid char => O(2^n)
        # optimal solution is to use DP and use an array to count
        # ways to decode starting from len(s)
        
        count_map = {len(s): 1}
        for idx in reversed(range(len(s))):
            if s[idx] == "0":
                count_map[idx] = 0
            else:
                count_map[idx] = count_map[idx+1]

                if idx+1 < len(s) and (s[idx] == "1" or (s[idx] == "2" and s[idx+1] in "0123456")):
                    count_map[idx] += count_map[idx+2]

        return count_map[0]
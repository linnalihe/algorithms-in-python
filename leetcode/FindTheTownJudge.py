
# Runtime: 704 ms, faster than 97.46% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19 MB, less than 23.34% of Python3 online submissions for Find the Town Judge.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustsOthers = set()
        trustCount = [0]*n

        for pair in trust:
            trustsOthers.add(pair[0]-1)
            trustCount[pair[1]-1] += 1

        for person in range(n):
            if person not in trustsOthers:
                if trustCount[person] == n-1:
                    return person+1

        return -1

    # n people labeled 1 to n
    # 1. the town judge trusts nobody
    # 2. everyone except town judge trusts town judge
    # there is only one person statisfying 1 and 2

    # Input: n = 2, trust = [[1,2]] (array of pairs, so an array of arrays)
    # Output: 2 , a trusts b for [a, b]
    # output should be the town judge if exist otherwise -1

    # if the town judge trusts noone, then when you iterate through array, for
    # n values that don't trust anyone, they are potential town judges

    # if everyone trusts judge, n values that have n-1 trusts are potential judge

    # iterate through trust list and tally if n trusts someone, track in set
    # iterate through trust list and tally number of people that trust n, track in array
    # [0, 1, 2, 3, 4, 5...]


# In a town, there are n people labelled from 1 to n.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:

# Input: n = 3, trust = [[1,2],[2,3]]
# Output: -1
# Example 5:

# Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3


# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= n


# solution by another RC member
class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        otherTrustCount = [False]*n

        for pair in trust:
            otherTrustCount[pair[0]-1] = True

        if otherTrustCount.count(False) != 1:
            return -1

        possible_judge = otherTrustCount.index(False) + 1
        count = 0
        for pair in trust:
            if pair[1] == possible_judge:
                count += 1

        if count == n-1:
            return possible_judge

        return -1

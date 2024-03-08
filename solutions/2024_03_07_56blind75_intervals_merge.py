# https://leetcode.com/problems/merge-intervals/
# all tests passed
def merge(intervals: list[list[int]]) -> list[list[int]]:
    output = []
    if len(intervals) < 1:
        return intervals

    intervals.sort()

    curr = intervals[0]
    for idx in range(1, len(intervals)):
        currstart, currend = curr
        nstart, nend = intervals[idx]

        if currend < nstart:
            output.append([currstart,currend])
            curr = [nstart, nend]
        elif currend >= nstart:
            curr = [min(currstart,nstart), max(currend,nend)]
        
    output.append(curr.copy())
    return output
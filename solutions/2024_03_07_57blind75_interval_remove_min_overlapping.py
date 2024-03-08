# https://leetcode.com/problems/non-overlapping-intervals/
# all tests passed
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:

    intervals.sort()
    count = 0
    currend = intervals[0][1]
    for idx in range(1, len(intervals)):
        nextstart = intervals[idx][0]
        nextend = intervals[idx][1]

        if currend <= nextstart:
            currend = nextend
        else:
            count+=1
            currend = min(currend, nextend)


    return count
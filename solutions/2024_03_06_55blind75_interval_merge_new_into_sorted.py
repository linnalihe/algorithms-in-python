# https://leetcode.com/problems/insert-interval/
# all tests passed
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    output = []

    for curridx in range(len(intervals)):
        start, end = intervals[curridx]
        nstart, nend = newInterval

        if nend < start:
            output.append(newInterval)
            return output + intervals[curridx:]

        elif end < nstart:
            output.append([start, end])
        else:
            newInterval = [min(start, nstart), max(end, nend)]

    output.append(newInterval)
    return output
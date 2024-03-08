# https://www.lintcode.com/problem/920/?source=激励弹窗分享
# all tests passed



class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        
        if len(intervals) <=1:
            return True
        intervals.sort(key=lambda x: x.start)
        for idx in range(len(intervals)-1):
            currend = intervals[idx].end
            nextstart = intervals[idx+1].start

            if currend > nextstart:
                return False

        return True
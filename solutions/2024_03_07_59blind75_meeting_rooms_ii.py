
# https://www.lintcode.com/problem/919
# all tests passed
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: list[Interval]) -> int:
        # at least one if no overlapping
        # count number to remove so no overlapping and then add 1
        res = 0
        
        startrange = sorted([s.start for s in intervals])
        endrange = sorted([e.end for e in intervals])

        starttime = 0
        endtime = 0
        count = 0
        while starttime < len(startrange):

            if startrange[starttime] < endrange[endtime]:
                count +=1
                starttime+=1
                res = max(res, count)
            else:
                count-=1
                endtime+=1
            
        return res
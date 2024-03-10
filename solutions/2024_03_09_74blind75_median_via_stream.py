# https://leetcode.com/problems/find-median-from-data-stream/
# all tests passed
import heapq
class MedianFinder:

    def __init__(self):
        self.smaller_maxheap = []
        self.larger_minheap = []
        
    def addNum(self, num: int) -> None:
        # check val minheap and val in maxheap
        heapq.heappush(self.smaller_maxheap, -1*num)

        if (self.smaller_maxheap and self.larger_minheap and 
        (-1*self.smaller_maxheap[0]) > self.larger_minheap[0]):
            n = -1*heapq.heappop(self.smaller_maxheap)
            heapq.heappush(self.larger_minheap, n)

        if len(self.smaller_maxheap) > len(self.larger_minheap) +1:
            n = -1*heapq.heappop(self.smaller_maxheap)
            heapq.heappush(self.larger_minheap, n)
        
        if len(self.larger_minheap) > len(self.smaller_maxheap)+1:
            n = heapq.heappop(self.larger_minheap)
            heapq.heappush(self.smaller_maxheap, -1*n)

        
    def findMedian(self) -> float:
        if len(self.larger_minheap) > len(self.smaller_maxheap):
            return self.larger_minheap[0]
        elif len(self.larger_minheap) < len(self.smaller_maxheap):
            return -1*self.smaller_maxheap[0]
        else:
            return (self.larger_minheap[0] + (-1*self.smaller_maxheap[0])) / 2
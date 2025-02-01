#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -value)
        
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            value = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, value)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end


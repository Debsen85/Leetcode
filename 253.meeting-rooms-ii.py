#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        for start, end in intervals:
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
# @lc code=end


#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = defaultdict(int)
        for task in tasks:
            taskMap[task] += 1
        currentIndex = 0
        maxHeap = []
        stack = []
        for task in taskMap:
            maxHeap.append((-taskMap[task], -1))
        heapq.heapify(maxHeap)
        while maxHeap:
            currentIndex += 1
            while maxHeap and maxHeap[0][1] != -1 and currentIndex - 1 - n < maxHeap[0][1]:
                stack.append(heapq.heappop(maxHeap))
            if maxHeap:
                frequency, index = heapq.heappop(maxHeap)
                frequency += 1
                index = currentIndex
                if frequency < 0:
                    heapq.heappush(maxHeap, (frequency, index))
            while stack:
                heapq.heappush(maxHeap, stack.pop())
        return currentIndex

# @lc code=end


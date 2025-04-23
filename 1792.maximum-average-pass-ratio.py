#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
from heapq import heappop, heappush
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        for passed, total in classes:
            current = passed / total
            after = (passed + 1) / (total + 1)
            delta = current - after
            heappush(maxHeap, (delta, passed, total))
        
        while extraStudents:
            extraStudents -= 1
            delta, passed, total = heappop(maxHeap)
            passed += 1
            total += 1
            current = passed / total
            after = (passed + 1) / (total + 1) 
            delta = current - after
            heappush(maxHeap, (delta, passed, total))
        
        answer = 0.0

        for delta, passed, total in maxHeap:
            answer += (passed / total)

        return answer / len(maxHeap)
# @lc code=end


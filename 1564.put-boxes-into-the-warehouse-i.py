#
# @lc app=leetcode id=1564 lang=python3
#
# [1564] Put Boxes Into the Warehouse I
#

# @lc code=start
import heapq
import math
from typing import List

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        answer, pinchPoint, minHeight = 0, [0] * len(warehouse), math.inf
        heapq.heapify(boxes)
        
        for index, height in enumerate(warehouse):
            minHeight = min(minHeight, height)
            pinchPoint[index] = minHeight

        for height in reversed(pinchPoint):
            if not boxes:
                break
            if boxes[0] <= height:
                heapq.heappop(boxes)
                answer += 1

        return answer

# @lc code=end


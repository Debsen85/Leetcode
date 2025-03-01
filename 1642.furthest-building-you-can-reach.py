#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        answer = 0

        for i in range(len(heights) -1):
            diff = heights[i + 1] - heights[i]

            if heights[i] < heights[i + 1]:
                if ladders:
                    heapq.heappush(minHeap, diff)
                    ladders -= 1
                else:
                    if minHeap:
                        if diff <= minHeap[0]:
                            if bricks >= diff:
                                bricks -= diff
                            else:
                                return answer
                        else:
                            if bricks >= minHeap[0]:
                                bricks -= heapq.heappop(minHeap)
                                heapq.heappush(minHeap, diff)
                            else:
                                return answer
                    else:
                        if bricks >= diff:
                            bricks -= diff
                        else:
                            return answer
            answer += 1
        return answer
# @lc code=end


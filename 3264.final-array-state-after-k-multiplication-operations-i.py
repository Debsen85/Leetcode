#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        for index, num in enumerate(nums):
            heapq.heappush(minHeap, (num, index))
        while k:
            value, index = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (value * multiplier, index))
            k -= 1
        while minHeap:
            value, index = heapq.heappop(minHeap)
            nums[index] = value
        return nums
# @lc code=end


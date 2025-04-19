#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
from heapq import heappop, heappush
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        visited = set()
        minHeap = []
        score = 0
        for index, num in enumerate(nums):
            heappush(minHeap, (num, index))
        while minHeap:
            value, index = heappop(minHeap)
            if index not in visited:
                score += value
                visited.add(index)
                visited.add(index + 1)
                visited.add(index - 1)
        return score
# @lc code=end


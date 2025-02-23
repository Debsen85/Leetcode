#
# @lc app=leetcode id=2599 lang=python3
#
# [2599] Make the Prefix Sum Non-negative
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        minHeap = []
        prefix = 0
        answer = 0

        for index in range(len(nums)):
            prefix += nums[index]
            if nums[index] < 0:
                heapq.heappush(minHeap, nums[index])
            if prefix < 0:
                prefix += -heapq.heappop(minHeap)
                answer += 1  

        return answer        
# @lc code=end


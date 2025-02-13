#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1 and nums[0] < k:
            a = heapq.heappop(nums) * 2
            b = heapq.heappop(nums)
            heapq.heappush(nums, a + b)
            operations += 1
        return operations
# @lc code=end


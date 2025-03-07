#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums) - k
        while k:
            heapq.heappop(nums)
            k -= 1
        return nums[0]
# @lc code=end


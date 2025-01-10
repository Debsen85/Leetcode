#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = -heapq.heappop(stones), -heapq.heappop(stones)
            heapq.heappush(stones, -(abs(a - b)))
        return -stones[0]

# @lc code=end
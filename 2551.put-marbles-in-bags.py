#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
from heapq import heappop, heappush
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        minHeap = []
        maxHeap = []
        for index in range(1, len(weights)):
            value = weights[index] + weights[index - 1]
            heappush(minHeap, value)
            heappush(maxHeap, -value)
        answer = 0
        while k - 1:
            answer += -heappop(maxHeap) - heappop(minHeap)
            k -= 1
        return answer
# @lc code=end


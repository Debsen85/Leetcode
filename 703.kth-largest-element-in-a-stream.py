#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.scores = nums
        self.highest = k
        heapq.heapify(self.scores)
        while len(self.scores) > self.highest:
            heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        heapq.heappush(self.scores, val)
        while len(self.scores) > self.highest:
            heapq.heappop(self.scores)
        return self.scores[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end


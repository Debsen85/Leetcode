#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L, R = 0, 0
        answer = []
        maxHeap = []
        heapq.heapify(maxHeap)
        while R < len(nums):
            heapq.heappush(maxHeap,[-nums[R], R])
            if R - L + 1 == k:
                while maxHeap[0][1] < L:
                    heapq.heappop(maxHeap)
                answer.append(-maxHeap[0][0])
                L += 1
            R += 1
        return answer
        
# @lc code=end



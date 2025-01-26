#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap, maxValue, result = [], 0, float('inf')

        for num in nums:
            temp = num
            while num % 2 == 0:
                num //= 2
            minHeap.append((num, max(num * 2, temp)))
            maxValue = max(maxValue, num)

        heapq.heapify(minHeap)

        while len(minHeap) == len(nums):
            num, numMax = heapq.heappop(minHeap)
            result = min(result, maxValue - num)
            
            if num < numMax:
                heapq.heappush(minHeap, ((num * 2), numMax))
                maxValue = max(maxValue, num * 2)
        
        return result

# @lc code=end


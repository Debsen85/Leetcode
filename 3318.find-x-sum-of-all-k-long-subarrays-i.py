#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            arrays = nums[i : i + k]
            arraysMap = defaultdict(int)
            for array in arrays:
                arraysMap[array] += 1
            answer = 0
            maxHeap = []
            for key in arraysMap:
                heappush(maxHeap, (-arraysMap[key], -key))
            answer, numberOfElements = 0, x
            while maxHeap and numberOfElements:
                numberOfElements -= 1
                frequency, value = heappop(maxHeap)
                answer += (frequency * value)
            result.append(answer)
        return result
# @lc code=end


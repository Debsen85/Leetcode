#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

# @lc code=start
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        arrayMap = {}

        nums = nums1 + nums2

        for key, value in nums:
            arrayMap[key] = arrayMap.get(key, 0) + value

        answer = []

        for key in arrayMap:
            answer.append([key, arrayMap[key]])
        
        return sorted(answer)
# @lc code=end


#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        numsMap = defaultdict(int)
        length = len(nums)
        for num in nums:
            numsMap[num] += 1
        maximum = 0
        frequency = 0
        for key in numsMap:
            if numsMap[key] > frequency:
                frequency = numsMap[key]
                maximum = key
        tillNow = 0
        for index, num in enumerate(nums):
            if num == maximum:
                tillNow += 1
                if tillNow * 2 > (index + 1) and (frequency - tillNow) * 2 > (length - index - 1):
                    return index
        return -1
# @lc code=end


#
# @lc app=leetcode id=1064 lang=python3
#
# [1064] Fixed Point
#

# @lc code=start
from typing import List

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for index, num in enumerate(arr):
            if index == num:
                return num
        return -1
# @lc code=end


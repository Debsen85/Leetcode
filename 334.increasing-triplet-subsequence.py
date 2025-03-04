#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = float('inf')
        for c in nums:
            if c <= a:
                a = c
            elif c <= b:
                b = c
            else:
                return True
        return False
# @lc code=end


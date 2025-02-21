#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        preHash = {}
        preHash[0] = 1
        prefix = 0
        res = 0
        for i, n in enumerate(nums):
            prefix += n
            if prefix == k:
                res = i + 1
            elif prefix - k in preHash:
                res = max(res, i - preHash[prefix - k])
            if prefix not in preHash:
                preHash[prefix] = i
        return res
# @lc code=end


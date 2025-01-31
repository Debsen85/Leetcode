#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preHash = {}
        preHash[0] = 1
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            res += preHash.get(prefix - k, 0)
            preHash[prefix] = 1 + preHash.get(prefix, 0)
        return res
# @lc code=end


#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(value):
            t = 0
            for candy in candies:
                t += candy // value
            return t
        
        if len(candies) == 1:
            return candies[0] // k

        l, r, result = 1, max(candies), 0
        while l <= r:
            m = (l + r) // 2
            j = check(m)
            if j >= k:
                result = m
                l = m + 1
            else:
                r = m - 1
        return result
# @lc code=end


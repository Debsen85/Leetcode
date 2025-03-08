#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List

class Solution:
    def findHours(self, nums, value):
        total = 0
        for n in nums:
            if n % value == 0:
                total += n // value
            else:
                total += ((n // value) + 1)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = 0
        while L <= R:
            M = (L + R) // 2

            check = self.findHours(piles, M)

            if check <= h:
                R = M - 1
                res = M

            else:
                L = M + 1
        
        return res

        
# @lc code=end


#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies) >= maxCandy
        return candies
# @lc code=end


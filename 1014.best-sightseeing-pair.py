#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values):
        result = 0
        curr = values[0] - 1
        for index in range(1, len(values)):
            result = max(result, curr + values[index])
            curr = max(values[index] - 1, curr - 1)
        return result
# @lc code=end
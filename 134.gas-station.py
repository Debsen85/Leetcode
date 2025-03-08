#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current = 0
        start = 0

        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                current  = 0
                start = i + 1

        return start
# @lc code=end


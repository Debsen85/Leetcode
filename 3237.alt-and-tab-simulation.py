#
# @lc app=leetcode id=3237 lang=python3
#
# [3237] Alt and Tab Simulation
#

# @lc code=start
from typing import List


class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        hashSet, answer = set(), []
        for query in reversed(queries):
            if query not in hashSet:
                answer.append(query)
                hashSet.add(query)
        for window in windows:
            if window not in hashSet:
                answer.append(window)
        return answer
# @lc code=end


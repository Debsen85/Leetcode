#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for _ in range(len(temperatures))]
        for i in reversed(range(len(temperatures))):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if stack:
                output[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return output

# @lc code=end


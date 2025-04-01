#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        def backtracking(index):
            if index >= len(questions):
                return 0
            if index in cache:
                return cache[index]
            cache[index] = max(questions[index][0] + backtracking(index + questions[index][1] + 1), backtracking(index + 1))
            return cache[index]
        return backtracking(0)
# @lc code=end


#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#

# @lc code=start
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        def prefixSum():
            for num1, num2 in zip(grid[0], grid[1]):
                prefix1.append(prefix1[-1] + num1)
                prefix2.append(prefix2[-1] + num2)

        def calculateMaxPathSum():
            answer = []
            for index in range(len(grid[0])):
                answer.append(max(prefix1[-1] - prefix1[index + 1], prefix2[index]))
            return min(answer)

        prefix1 = [0]
        prefix2 = [0]

        prefixSum()

        return calculateMaxPathSum()
# @lc code=end


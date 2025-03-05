#
# @lc app=leetcode id=2579 lang=python3
#
# [2579] Count Total Number of Colored Cells
#

# @lc code=start
class Solution:
    def coloredCells(self, n: int) -> int:
        answer = 1
        current = 1
        while current < n:
            answer += current * 4
            current += 1
        return answer
# @lc code=end


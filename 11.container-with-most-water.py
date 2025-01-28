#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        answer = 0
        while L < R:
            answer = max(answer, min(height[L], height[R]) * (R - L))
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return answer        
# @lc code=end


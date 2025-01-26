#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        L, R = 0, len(height) - 1
        maxLeft, maxRight = height[L], height[R]
        answer = 0

        while (L < R):

            if maxLeft <= maxRight:
                L += 1
                maxLeft = max(maxLeft, height[L])
                answer += maxLeft - height[L] if maxLeft - height[L] > 0 else 0

            else:
                R -= 1
                maxRight = max(maxRight, height[R])
                answer += maxRight - height[R] if maxRight - height[R] > 0 else 0

        return answer
        
# @lc code=end


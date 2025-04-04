#
# @lc app=leetcode id=3285 lang=python3
#
# [3285] Find Indices of Stable Mountains
#

# @lc code=start
from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = []
        for index in range(1, len(height)):
            if height[index - 1] > threshold:
                answer.append(index)
        return answer
# @lc code=end


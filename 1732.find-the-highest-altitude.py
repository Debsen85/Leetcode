#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = 0
        prefix = 0
        for gains in gain:
            prefix += gains
            answer = max(answer, prefix)
        return answer

# @lc code=end


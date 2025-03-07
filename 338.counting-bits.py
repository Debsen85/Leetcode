#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        while n >= 0:
            output.append(bin(n)[2:].count('1'))
            n -= 1
        return output[::-1]
# @lc code=end


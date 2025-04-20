#
# @lc app=leetcode id=781 lang=python3
#
# [781] Rabbits in Forest
#

# @lc code=start
from collections import Counter
from math import ceil
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0
        for k, v in freq.items():
            group_size = k + 1
            groups = ceil(v / group_size)
            total += groups * group_size
        return total
# @lc code=end


#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = [differences[0]]
        for difference in differences[1:]:
            prefix.append(prefix[-1] + difference)
        maximum, minimum = max(prefix), min(prefix)
        answer = 0
        for value in range(lower, upper + 1, 1):
            if (lower <= (value + minimum) <= upper) and (lower <= (value + maximum) <= upper):
                answer += 1
        return answer
# @lc code=end


#
# @lc app=leetcode id=3184 lang=python3
#
# [3184] Count Pairs That Form a Complete Day I
#

# @lc code=start
from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        answer = 0
        for i in range(len(hours) - 1):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0: answer += 1
        return answer
# @lc code=end


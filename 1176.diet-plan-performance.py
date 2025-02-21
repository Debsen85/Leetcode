#
# @lc app=leetcode id=1176 lang=python3
#
# [1176] Diet Plan Performance
#

# @lc code=start
from typing import List

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        i = 0
        j = 0
        answer = 0
        current = 0
        while j < len(calories):
            current += calories[j]
            if j - i + 1 > k:
                current -= calories[i]
                i += 1
            if j - i + 1 == k:
                if current < lower:
                    answer -= 1
                elif current > upper:
                    answer += 1
            j += 1
        return answer
# @lc code=end


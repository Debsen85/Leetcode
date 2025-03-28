#
# @lc app=leetcode id=3386 lang=python3
#
# [3386] Button with Longest Push Time
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prev, total, answer = 0, 0, events[0][0]
        for index, time in events:
            if total < time - prev:
                answer = index
                total = time - prev
            elif total == time - prev:
                answer = min(answer, index)
            prev = time
        return answer
# @lc code=end


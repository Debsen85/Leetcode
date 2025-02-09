#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        answer = 0
        previousEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if previousEnd > start:
                answer += 1
                previousEnd = min(previousEnd, end)
            else:
                previousEnd = end
        return answer
# @lc code=end


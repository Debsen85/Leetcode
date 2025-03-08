#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                intervals[i][0] = max(intervals[i][0], intervals[i - 1][0])
                intervals[i][1] = min(intervals[i][1], intervals[i - 1][1])
                answer += 1
        
        return answer
        
# @lc code=end


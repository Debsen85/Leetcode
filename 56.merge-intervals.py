#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        answer = []
        for i in range(len(intervals) - 1):
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
            else:
                answer.append(intervals[i])
        answer.append(intervals[i + 1])
        return answer
# @lc code=end


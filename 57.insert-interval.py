#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        answer = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                answer.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                i -= 1
                break
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        return answer + [newInterval] + intervals[i + 1 : ]

# @lc code=end


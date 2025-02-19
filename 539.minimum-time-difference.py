#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for point in timePoints:
            times.append(int(point[:2]) * 60 + int(point[3:]))
        times.sort()
        answer = 1440
        for i in range(len(times) - 1):
            if i == 0:
                answer = min(answer, min(abs(1440 - times[-1] + times[i]), times[i + 1] - times[i]))
            else:
                answer = min(answer, times[i + 1] - times[i])
        return answer
        # @lc code=end


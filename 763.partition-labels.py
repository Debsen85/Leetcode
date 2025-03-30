#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List

class Solution:
    def partitionLabels(self, string: str) -> List[int]:
        last = [-1] * 26
        first = [-1] * 26
        l, r = 0, len(string) - 1
        while l < len(string) and r >= 0:
            a = ord(string[l]) - 97
            b = ord(string[r]) - 97
            if first[a] == -1:
                first[a] = l
            if last[b] == -1:
                last[b] = r
            l += 1
            r -= 1
        intervals = []
        for s, e in zip(first, last):
            if s != -1 and e != -1:
                intervals.append([s, e])
        intervals.sort()
        answer = []
        for index in range(1, len(intervals)):
            if intervals[index][0] < intervals[index - 1][1]:
                intervals[index][0] = min(intervals[index][0], intervals[index - 1][0])
                intervals[index][1] = max(intervals[index][1], intervals[index - 1][1])
            else:
                answer.append(intervals[index - 1][1] - intervals[index - 1][0] + 1)
        answer.append(intervals[-1][1] - intervals[-1][0] + 1)
        return answer
# @lc code=end


#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        newMeetings = []
        for index in range(1, len(meetings)):
            if meetings[index][0] <= meetings[index - 1][1]:
                meetings[index][0] = min(meetings[index][0], meetings[index - 1][0])
                meetings[index][1] = max(meetings[index][1], meetings[index - 1][1])
            else:
                newMeetings.append(meetings[index - 1])
        newMeetings.append(meetings[-1])
        for start, end in newMeetings:
            days -= (end - start + 1)
        return days
# @lc code=end


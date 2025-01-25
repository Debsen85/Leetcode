#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        val = tickets[k]
        for i in range(len(tickets)):
            if i == k:
                continue
            elif i < k:
                tickets[i] = val if val < tickets[i] else tickets[i]
            else:
                tickets[i] = val - 1 if val <= tickets[i] else tickets[i]
        return sum(tickets)
# @lc code=end


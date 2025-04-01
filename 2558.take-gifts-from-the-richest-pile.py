#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
from heapq import heapify, heappop, heappush
from math import sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapify(gifts)
        while k:
            gift = -heappop(gifts)
            gift = int(sqrt(gift))
            heappush(gifts, -gift)
            k -= 1
        return -sum(list(gifts))
# @lc code=end


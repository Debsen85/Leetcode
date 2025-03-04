#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        while i < length and n:
            if flowerbed[i] == 0 and ((i - 1) < 0 or flowerbed[i - 1] == 0) and ((i + 1) == length or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1
        return not n

# @lc code=end


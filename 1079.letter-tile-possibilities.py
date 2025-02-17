#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
from typing import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        countMap = Counter(tiles)
        def backtracking():
            result = 0
            for tile in countMap:
                if countMap[tile]:
                    countMap[tile] -= 1
                    result += 1
                    result += backtracking()
                    countMap[tile] += 1
            return result             
        return backtracking()
# @lc code=end


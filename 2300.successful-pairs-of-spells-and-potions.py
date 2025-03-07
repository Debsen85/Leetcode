#
# @lc app=leetcode id=2300 lang=python3
#
# [2300] Successful Pairs of Spells and Potions
#

# @lc code=start
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        answer = []

        for spell in spells:
            left, right, result = 0, length - 1, 0

            while(left <= right):
                middle = (left + right) // 2

                if potions[middle] * spell < success:
                    left = middle + 1
                    result = left
                else:
                    right = middle - 1
                    
            answer.append(len(potions) - result)

        return answer 
# @lc code=end


#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]

            if total == target:
                return [L + 1, R + 1]
            
            elif total > target:
                R -= 1
            
            else:
                L += 1
        
# @lc code=end


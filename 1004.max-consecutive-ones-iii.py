#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        zero = 0
        answer, total = 0, 0

        while j < len(nums):
            if nums[j] == 0:
                zero += 1
            total += 1

            while zero > k:
                if nums[i] == 0:
                    zero -= 1
                i += 1
                total -= 1
            
            answer = max(answer, total)

            j += 1
        
        return answer
# @lc code=end


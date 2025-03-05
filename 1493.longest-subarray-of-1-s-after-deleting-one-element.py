#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        zero, total, answer = 0, 0, 0

        while j < len(nums):
            if nums[j] == 0:
                zero += 1
            
            else:
                total += 1

            while zero > 1:
                if nums[i] == 0:
                    zero -= 1
                else:
                    total -= 1
                i += 1

            answer = max(answer, total if zero else total - 1)

            j += 1

        return answer
# @lc code=end


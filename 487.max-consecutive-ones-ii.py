#
# @lc app=leetcode id=487 lang=python3
#
# [487] Max Consecutive Ones II
#

# @lc code=start
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        zero = 0
        answer = 0
        j = 0

        while j < len(nums):
            while j < len(nums) and nums[j] == 1:
                curr += 1
                j += 1

            if not prev:
                prev = curr
                if not zero:
                    answer = max(answer, prev)
                else:
                    answer = max(answer, prev + 1)
            else:
                if zero == 1:
                    answer = max(answer, prev + curr + 1)
                else:
                    answer = max(answer, curr + 1)
                prev = curr
            zero = 0
            curr = 0

            while j < len(nums) and nums[j] == 0:
                zero += 1
                j += 1

        if zero == 1:
            answer = max(answer, prev + curr + 1)
        elif zero > 1:
            answer = max(answer, prev + 1)

        return answer
        
# @lc code=end


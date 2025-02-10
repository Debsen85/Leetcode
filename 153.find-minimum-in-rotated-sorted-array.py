#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        answer = nums[0]
        while L <= R:
            if nums[L] < nums[R]:
                answer = min(answer, nums[L])
                break
            M = (L + R) // 2
            answer = min(answer, nums[M])
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1
        return answer
            

# @lc code=end


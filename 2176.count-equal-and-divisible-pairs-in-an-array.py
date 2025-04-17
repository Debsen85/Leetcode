#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        c += 1
        return c
# @lc code=end


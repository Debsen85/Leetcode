#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(3)] for _ in range(len(nums))]
        def backtracking(index, count):
            if index < 0 or count == 3:
                return 0
            if dp[index][count] != -1:
                return dp[index][count]
            if count == 0:
                dp[index][count] = max(backtracking(index - 1, count), nums[index] * backtracking(index - 1, count + 1))
            elif count == 1:
                dp[index][count] = max(backtracking(index - 1, count), backtracking(index - 1, count + 1) - nums[index])
            else:
                dp[index][count] = max(backtracking(index - 1, count), backtracking(index - 1, count + 1) + nums[index])
            return dp[index][count]
        return backtracking(len(nums) - 1, 0)
# @lc code=end


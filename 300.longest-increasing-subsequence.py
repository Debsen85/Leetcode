#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        dp = {}

        def backtracking(i):
            if i in dp:
                return dp[i]

            if i == len(nums):
                return 0

            res = 0

            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, 1 + backtracking(j))

            dp[i] = res
            return res

        for i in range(len(nums)):
            ans = max(ans, 1 + backtracking(i))

        return ans
# @lc code=end


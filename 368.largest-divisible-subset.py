#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cache = {}
        def backtracking(index, prev):
            if index == len(nums):
                return [] 
            if (index, prev) in cache:
                return cache[(index, prev)]
            skip = backtracking(index + 1, prev)
            take = []
            if prev == -1:
                take = [nums[index]] + backtracking(index + 1, index)
            elif prev != -1 and nums[index] % nums[prev] == 0:
                take = [nums[index]] + backtracking(index + 1, index)
            cache[(index, prev)] = max(skip, take, key=len)
            return cache[(index, prev)]     
        backtracking(0, -1)
        return backtracking(0, -1)
# @lc code=end


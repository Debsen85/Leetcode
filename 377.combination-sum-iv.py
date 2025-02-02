#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        answer = {}
        return self.backtracking(nums, target, answer)
    
    def backtracking(self, nums, target, answer):
        if target == 0:
            return 1
        if target < 0:
            return 0
        if target in answer:
            return answer[target]
        output = 0
        for num in nums:
            output += self.backtracking(nums, target - num, answer)
        answer[target] = output
        return output
        
        
        
# @lc code=end


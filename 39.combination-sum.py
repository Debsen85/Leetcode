#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtracking(i, current, total):
            if total == target:
                answer.append(current[:])
                return
            
            if i == len(candidates) or total > target:
                return
            
            current.append(candidates[i])
            backtracking(i, current, total + candidates[i])
            current.pop()
            backtracking(i + 1, current, total)
        
        backtracking(0, [], 0)
        return answer
        
# @lc code=end


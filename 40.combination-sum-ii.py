#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        candidates.sort()
        def backtracking(i, current, total):
            if total == target:
                answer.add(tuple(current[:]))
                return
            if i == len(candidates) or total > target:
                return
            current.append(candidates[i])
            backtracking(i + 1, current, total + candidates[i])
            current.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(i + 1, current, total)
        backtracking(0, [], 0)
        return list(answer)
            
# @lc code=end


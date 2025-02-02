#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtracking(index, combo):
            if len(combo) == k:
                answer.append(combo[:])
                return
            if len(combo) > k or index > n:
                return
            
            combo.append(index)
            backtracking(index + 1, combo)
            combo.pop()
            backtracking(index + 1, combo)

        backtracking(1, [])
        return answer
# @lc code=end


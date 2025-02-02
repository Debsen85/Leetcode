#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        def backtracking(i, current, total):
            if total == n:
                if len(current) == k:
                    answer.append(current[:])
                return
            if i == 10 or total > n:
                return
            current.append(i)
            backtracking(i + 1, current, total + i)
            current.pop()
            backtracking(i + 1, current, total)
        backtracking(1, [], 0)
        return answer
# @lc code=end


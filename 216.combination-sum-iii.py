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

        def backtracking(value, current, n):
            if len(current) == k and n == 0:
                answer.append(current[:])
                return
            if len(current) > k or n < 0 or value == 10:
                return
            
            current.append(value)
            backtracking(value + 1, current, n - value)

            current.pop()
            backtracking(value + 1, current, n)
            
        backtracking(1, [], n)
        return answer
# @lc code=end


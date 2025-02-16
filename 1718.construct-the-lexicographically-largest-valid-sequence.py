#
# @lc app=leetcode id=1718 lang=python3
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#

# @lc code=start
from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        answer = [0] * (n * 2 - 1)
        have = set()

        def backtracking(index):
            if index == len(answer):
                return True
            for j in reversed(range(1, n + 1)):
                if j in have:
                    continue
                if j > 1 and (index + j >= len(answer) or answer[index + j]):
                    continue
                have.add(j)
                answer[index] = j
                if j > 1:
                    answer[index + j] = j
                k = index + 1
                while k < len(answer) and answer[k]:
                    k += 1
                if backtracking(k):
                    return True
                have.remove(j)
                answer[index] = 0
                if j > 1:
                    answer[index + j] = 0
            return False
        backtracking(0)
        return answer
# @lc code=end


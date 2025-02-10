#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List

class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        answer = []
        def backtracking(i, subAnswer):
            if i == len(s):
                answer.append(subAnswer[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    subAnswer.append(s[i : j + 1])
                    backtracking(j + 1, subAnswer)
                    subAnswer.pop()
        backtracking(0, [])
        return answer
# @lc code=end


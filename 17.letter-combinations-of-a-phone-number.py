#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        answer = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtracking(i, current):
            if len(current) == len(digits):
                answer.append("".join(current))
                return 
            if i == len(digits):
                return
            for value in phone[digits[i]]:
                current.append(value)
                backtracking(i + 1, current)
                current.pop()
        backtracking(0, [])
        return answer
# @lc code=end


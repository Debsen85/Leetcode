#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        result = deque()
        current = ""
        added = False
        for letter in s:
            if letter != " ":
                added = False
                current += letter
            elif not added:
                added = True
                result.appendleft(current)
                current = ""
        result.appendleft(current)
        return " ".join(list(result)).strip()
# @lc code=end


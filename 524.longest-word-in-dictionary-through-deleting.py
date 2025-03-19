#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#

# @lc code=start
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        answer = ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(word) and j < len(s):
                if s[j] == word[i]:
                    i += 1
                j += 1
            if i == len(word):
                if len(answer) < len(word):
                    answer = word
                elif len(answer) == len(word):
                    answer = min(answer, word)
        return answer
# @lc code=end


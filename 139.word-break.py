#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {} 
        def backtrack(index):
            if index == len(s):
                return True

            if index in dp:
                return dp[index]

            for word in wordDict:
                if (len(s) - index) >= len(word) and s[index : index + len(word)] == word:
                    if backtrack(index + len(word)):
                        dp[index] = True
                        return True
            dp[index] = False
            return False
        return backtrack(0)
# @lc code=end


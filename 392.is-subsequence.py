#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = {}

        def backtracking(i, j):
            if i == len(s) or j == len(t):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = 1 + backtracking(i + 1, j + 1)
            else:
                dp[(i, j)] = max(backtracking(i, j + 1), backtracking(i + 1, j))
            
            return dp[(i, j)]
        
        return len(s) == backtracking(0, 0)
# @lc code=end


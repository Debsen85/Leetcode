#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if  len(s1) + len(s2) != len(s3):
            return False
        cache = {}
        def backtracking(i, j, k):
            if k == len(s3):
                return ((len(s1) == i) and (len(s2) == j))
            if (i, j) in cache:
                return cache[(i, j)]
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = backtracking(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = backtracking(i, j + 1, k + 1)
            cache[(i, j)] = res
            return res
        return backtracking(0, 0, 0)
# @lc code=end


#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[-1] * len(word2) for _ in range(len(word1))]
        def bactracking(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if cache[i][j] != -1:
                return cache[i][j]
            if word1[i] == word2[j]:
                cache[i][j] = bactracking(i + 1, j + 1)
            else:
                res = min(bactracking(i + 1, j), bactracking(i, j + 1))
                res = min(res, bactracking(i + 1, j + 1))
                cache[i][j] = res + 1
            return cache[i][j]
        return bactracking(0, 0)
        
# @lc code=end


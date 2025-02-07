#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # ans = [0]
        # def backtracking(index,  subsequence):
        #     if index == len(s):
        #         if subsequence == subsequence[::-1] and len(subsequence) > ans[0]:
        #             ans[0] = len(subsequence)
        #         return
        #     subsequence.append(s[index])
        #     backtracking(index + 1, subsequence)
        #     subsequence.pop()
        #     backtracking(index + 1, subsequence)
        # backtracking(0, [])
        # return ans[0]

        length = len(s)
        cache = [[-1] * length for _ in range(length)]

        def backtracking(i, j):
            if i < 0 or j == length:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if s[i] == s[j]:
                total = 1 if i == j else 2
                cache[i][j] = total + backtracking(i - 1, j + 1)
            else:
                cache[i][j] = max(backtracking(i - 1, j), backtracking(i, j + 1))

            return cache[i][j]
        
        for i in range(length):
            backtracking(i, i)
            backtracking(i, i + 1)

        return max(max(row) for row in cache)

        
# @lc code=end


#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)

        dp = [[""] * (n2 + 1) for _ in range(2)]
        substitute = [""] * (n2 + 1)

        for i in range(n2 + 1):
            dp[1][n2 - i] = str2[n2 - i :]

        for i in range(n1 - 1, -1, -1):
            dp[0][n2] = str1[i : ]

            for j in range(n2 - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[0][j] = str1[i] + dp[1][j + 1]
                else:
                    if len(dp[1][j]) <= len(dp[0][j + 1]):
                        dp[0][j] = str1[i] + dp[1][j]
                    else:
                        dp[0][j] = str2[j] + dp[0][j + 1]
            dp[1] = dp[0].copy()
            dp[0] = substitute.copy()

        return dp[1][0]
# @lc code=end


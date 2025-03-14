#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        mapper = {}
        dp = {}
        for index, value in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):  
            mapper[str(index + 1)] = value

        def backtracking(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in dp:
                return dp[index]

            result = 0

            if s[index] in mapper:
                result += backtracking(index + 1)

            if index < len(s) - 1 and s[index : index + 2] in mapper:
                result += backtracking(index + 2)
            
            dp[index] = result
            return result

        return backtracking(0)
# @lc code=end


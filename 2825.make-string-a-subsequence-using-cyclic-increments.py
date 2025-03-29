#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        if n < m:
            return False
        i, j = 0, 0
        diff = []
        while i < n and j < m:
            value = None
            if str1[i] > str2[j]:
                value = 26 - (ord(str1[i]) - ord(str2[j]))
            elif str1[i] < str2[j]:
                value = ord(str2[j]) - ord(str1[i])
            else:
                value = 0
            if value < 2:
                diff.append(value)
                j += 1
            i += 1
        return len(diff) == m
# @lc code=end


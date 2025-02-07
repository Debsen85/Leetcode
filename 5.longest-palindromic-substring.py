#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        L, R = 0, 0
        maxLength = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    maxLength = r - l + 1
                    L, R = l, r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLength:
                    maxLength = r - l + 1
                    L, R = l, r
                l -= 1
                r += 1
        return s[L : R + 1]
# @lc code=end


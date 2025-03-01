#
# @lc app=leetcode id=2414 lang=python3
#
# [2414] Length of the Longest Alphabetical Continuous Substring
#

# @lc code=start
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        current, answer = 1, 1
        for i in range(len(s) - 1):
            if ord(s[i + 1]) - ord(s[i]) == 1:
                current += 1
            else:
                answer = max(answer, current)
                current = 1
        return max(answer, current)
# @lc code=end


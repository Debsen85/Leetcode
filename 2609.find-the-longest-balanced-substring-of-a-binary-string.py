#
# @lc app=leetcode id=2609 lang=python3
#
# [2609] Find the Longest Balanced Substring of a Binary String
#

# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        answer = 0
        zero = 0
        one = 0

        i, j = 0, 0

        while j < len(s):
            while j < len(s) and s[j] == '0':
                j += 1
            zero = j - i
            i = j

            while j < len(s) and s[j] == '1':
                j += 1
            one = j - i
            i = j

            answer = max(answer, min(zero, one) * 2)
        
        return answer
# @lc code=end


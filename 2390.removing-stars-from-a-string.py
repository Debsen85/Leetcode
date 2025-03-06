#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for letter in s:
            if letter != '*':
                stack.append(letter)
            elif stack:
                stack.pop()
        
        return ''.join(stack)
# @lc code=end


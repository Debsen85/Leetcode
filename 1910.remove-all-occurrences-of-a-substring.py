#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        stack = []
        length = len(part)
        for letter in s:
            stack.append(letter)
            if stack[-length :] == part:
                time = length
                while time:
                    stack.pop()
                    time -= 1
        return ''.join(stack)
# @lc code=end


#
# @lc app=leetcode id=1165 lang=python3
#
# [1165] Single-Row Keyboard
#

# @lc code=start
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        diff, curr = 0, 0
        for w in word:
            index = keyboard.index(w)
            diff += abs(curr - index)
            curr = index
        return diff
# @lc code=end


#
# @lc app=leetcode id=3360 lang=python3
#
# [3360] Stone Removal Game
#

# @lc code=start
class Solution:
    def canAliceWin(self, n: int) -> bool:
        current = "Alice"
        turn  = 10

        while n >= turn:
            n -= turn
            if current == "Alice":
                current = "Bob"
            else:
                current = "Alice"
            turn -= 1
        
        return not current == "Alice"
        
# @lc code=end


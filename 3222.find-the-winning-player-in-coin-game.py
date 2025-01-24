#
# @lc app=leetcode id=3222 lang=python3
#
# [3222] Find the Winning Player in Coin Game
#

# @lc code=start
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:

        currPlayer = "Bob"

        while True:

            if x - 1 < 0 or y - 4 < 0:
                return currPlayer
            
            else:
                if currPlayer == "Bob" :
                    currPlayer = "Alice"
                else:
                    currPlayer = "Bob"
                
                x -= 1
                y -= 4
        
# @lc code=end


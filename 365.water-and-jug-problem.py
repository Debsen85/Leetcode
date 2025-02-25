#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def gcd(self, x, y):
        if y % x == 0:
            return x
        return self.gcd(y % x, x)

    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if x + y == target or x == target or y == target:
            return True
        else:
            return (target % self.gcd(min(x, y), max(x, y)) == 0)
        

        
# @lc code=end


#
# @lc app=leetcode id=2417 lang=python3
#
# [2417] Closest Fair Integer
#

# @lc code=start
class Solution:
    def countEvenOdd(self, num):
        even, odd = 0, 0
        while num:
            d = num % 10
            if d % 2: odd += 1
            else: even += 1
            num //= 10
        return odd == even

    def closestFair(self, n: int) -> int:
        while True:
            if len(str(n)) % 2 == 0:
                if self.countEvenOdd(n): return n
                else: n += 1
            else:
                n = 10 ** len(str(n))
        
# @lc code=end


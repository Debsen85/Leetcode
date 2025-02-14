#
# @lc app=leetcode id=1352 lang=python3
#
# [1352] Product of the Last K Numbers
#

# @lc code=start
from collections import deque

class ProductOfNumbers:

    def __init__(self):
        self.actualProduct = []
        self.zeroTracker = []
        self.size = 0

    def add(self, num: int) -> None:
        self.actualProduct.append((self.actualProduct[-1] if self.actualProduct else 1) * (num if num > 0 else 1))
        if num == 0: 
            self.zeroTracker.append(self.size)
        self.size += 1

    def getProduct(self, k: int) -> int:
        if self.zeroTracker and self.size - k - 1 < self.zeroTracker[-1] < self.size:
            return 0
        return (self.actualProduct[-1] // self.actualProduct[self.size - k - 1]) if self.size > k else self.actualProduct[-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end


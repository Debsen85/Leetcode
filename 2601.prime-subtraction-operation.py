#
# @lc app=leetcode id=2601 lang=python3
#
# [2601] Prime Subtraction Operation
#

# @lc code=start
from cmath import sqrt
from typing import List

class Solution:
    def __init__(self):
        self.sieve = [True for _ in range(1001)]
        self.sieve[0] = False
        self.sieve[1] = False
        for num in range(2, int(sqrt(1000)) + 1):
            for num in range(num + num, 1001, num):
                self.sieve[num] = False

    def primeSubOperation(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            l, r, result = 2, num - 1, 0
            for prime in reversed(range(2, min(num, 1001))):
                if index == 0:
                    if self.sieve[prime]:
                        nums[index] = nums[index] - prime
                        break
                else:
                    if self.sieve[prime] and nums[index - 1] < (nums[index] - prime):
                        nums[index] = nums[index] - prime
                        break
    
        for index in range(1, len(nums)):
            if nums[index] <= nums[index - 1]:
                return False
        return True
# @lc code=end


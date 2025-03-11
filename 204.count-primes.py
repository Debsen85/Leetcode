#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
from cmath import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        num_marks = [0,0] + [1] * (n-2)

        res = 0

        for num in range(2, int(sqrt(n))+1):
            if num_marks[num] == 1:
                res += 1

                for mul in range(num**2, n, num):
                    num_marks[mul] = 0
        
        return sum(num_marks)

# @lc code=end


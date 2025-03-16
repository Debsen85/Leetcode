#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#

# @lc code=start

from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def countOfCars(time):
            numberOfCars = 0
            for rank in ranks:
                numberOfCars += int((time // rank) ** 0.5)
            return cars <= numberOfCars

        left, right, result = 1, max(ranks) * cars * cars, 1

        while left <= right:

            time = (left + right) // 2

            if (countOfCars(time)):
                result = time
                right = time - 1
            else:
                left = time + 1
        
        return result
# @lc code=end


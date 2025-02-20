
#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#

# @lc code=start
from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {len(arr) : 0}
        def backtracking(i):
            if i in cache:
                return cache[i]
            currentMax = 0
            result = 0
            for j in range(i, min(i + k, len(arr))):
                currentMax = max(currentMax, arr[j])
                window = j - i + 1
                result = max(result, backtracking(j + 1) + currentMax * window)
            cache[i] = result
            return result
        return backtracking(0)
# @lc code=end


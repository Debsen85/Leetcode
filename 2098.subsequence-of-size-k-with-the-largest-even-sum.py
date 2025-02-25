#
# @lc app=leetcode id=2098 lang=python3
#
# [2098] Subsequence of Size K With the Largest Even Sum
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        total = sum(nums[ : k])

        if total % 2 == 0:
            return total

        minEven, minOdd = 10 ** 6, 10 ** 6

        for i in range(k):
            if nums[i] % 2:
                minOdd = min(minOdd, nums[i])
            else:
                minEven = min(minEven, nums[i])
        
        answer = -1

        for i in range(k, len(nums)):
            if nums[i] % 2 and minEven != 10 ** 6:
                answer = max(answer, total - minEven + nums[i])
            if nums[i] % 2 == 0 and minOdd != 10 ** 6:
                answer = max(answer, total - minOdd + nums[i])
        
        return answer
        
# @lc code=end


#
# @lc app=leetcode id=3364 lang=python3
#
# [3364] Minimum Positive Sum Subarray 
#

# @lc code=start
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        prefixSum =[0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        answer = 10 ** 9
        for i in range(1, len(prefixSum)):
            for j in range(i, len(prefixSum)):
                if r >= j - i + 1 >= l:
                    answer = min(answer, (prefixSum[j] - prefixSum[i - 1]) if prefixSum[j] - prefixSum[i - 1] > 0 else answer)
                if r < j - i + 1:
                    break
        return answer if answer != 10 ** 9 else -1
        # @lc code=end


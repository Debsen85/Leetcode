#
# @lc app=leetcode id=3354 lang=python3
#
# [3354] Make Array Elements Equal to Zero
#

# @lc code=start
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        if prefixSum[-1] == 0:
            return len(nums) * 2
        if prefixSum[-1] == 1:
            return len(nums) - 1 
        
        answer = 0

        for i in range(1, len(nums) - 1):
            print(i, nums[i], prefixSum[i], prefixSum[-1] - prefixSum[i])
            if nums[i] == 0:
                if prefixSum[i] == (prefixSum[-1] - prefixSum[i]):
                    answer += 2
                elif abs(prefixSum[i] - (prefixSum[-1] - prefixSum[i])) == 1:
                    answer += 1
                    
        return answer

# @lc code=end


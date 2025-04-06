#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        answer = 0
        currSum = 0
        hashMap = defaultdict(int)
        
        while j < len(nums):
            currSum += nums[j]
            hashMap[nums[j]] += 1
            while (hashMap[nums[j]] > 1) or (j - i + 1 > k):
                currSum -= nums[i]
                hashMap[nums[i]] -= 1
                i += 1
            if j - i + 1 == k:
                answer = max(answer, currSum)
            j += 1
        return answer


# @lc code=end


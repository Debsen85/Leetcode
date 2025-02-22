#
# @lc app=leetcode id=1852 lang=python3
#
# [1852] Distinct Numbers in Each Subarray
#

# @lc code=start
from typing import List

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        hashSet = {}
        total = 0
        answer = []
        i, j = 0, 0
        while j < len(nums):
            if hashSet.get(nums[j], 0) == 0:
                total += 1

            hashSet[nums[j]] = 1 + hashSet.get(nums[j], 0)

            if j - i + 1 > k and nums[i] in hashSet:
                hashSet[nums[i]] -= 1

                if hashSet[nums[i]] == 0:
                    total -= 1

                i += 1
                
            if j - i + 1 == k:
                answer.append(total)

            j += 1

        return answer
# @lc code=end


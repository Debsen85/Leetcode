#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        operations, index, flag = 0, 0, True
        while True:
            total = 0
            for key in hashMap:
                if hashMap[key] > 1:
                    total += 1
            if total > 0:
                for i in range(index, min(index + 3, len(nums))):
                    hashMap[nums[i]] -= 1
                operations += 1
                index += 3
            else:
                return  operations
        return -1
                
# @lc code=end


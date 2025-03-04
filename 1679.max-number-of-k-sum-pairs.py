#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        operations = 0

        for num in nums:
            if k <= num:
                continue
            if k - num == num:
                if hashMap[num] > 1:
                    operations += hashMap[num] // 2
                    hashMap[num] = hashMap[num] % 2
            else:
                if (k - num) in hashMap and hashMap[num] > 0 and hashMap[k - num] > 0:
                    value = min(hashMap[num], hashMap[k - num])
                    operations += value
                    hashMap[num] = hashMap[num] - value
                    hashMap[k - num] = hashMap[k - num] - value

        return operations
# @lc code=end


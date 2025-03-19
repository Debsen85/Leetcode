#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        length = len(nums)

        for num in nums:
            if num % 2:
                prefix.append(total)
                prefix.append(-1)
                total = 0
            else:
                total += 1
        if total:
            prefix.append(total)

        total = 0
        
        if prefix[0] == -1:
            l, r = 0, 2 * (k - 1)
        else:
            l, r = 1, 2 * (k - 1) + 1

        if r >= len(prefix):
            return 0

        a, b = 1, 1
        while r < len(prefix):
            if l > 0 and prefix[l - 1] != -1:
                a += prefix[l - 1]
            if r < len(prefix) - 1 and prefix[r + 1] != -1:
                b += prefix[r + 1]
            total += (a * b)
            a, b = 1, 1
            l += 2
            r += 2
            
        return total
# @lc code=end


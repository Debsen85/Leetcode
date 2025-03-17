#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            i = m - 1
            j = n - 1
            r = m + n - 1
            while j >= 0 and i >= 0:
                if nums1[i] <= nums2[j]:
                    nums1[r] = nums2[j]
                    j -= 1
                else:
                    nums1[r] = nums1[i]
                    i -= 1
                r -= 1
            while j >= 0:
                nums1[r] = nums2[j]
                j -= 1
                r -= 1
        
# @lc code=end


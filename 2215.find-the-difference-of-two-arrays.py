#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans1 = []
        ans2 = []

        for num in nums1:
            if num not in nums2:
                ans1.append(num)

        for num in nums2:
            if num not in nums1:
                ans2.append(num)

        return [ans1, ans2]
# @lc code=end


#
# @lc app=leetcode id=1981 lang=python3
#
# [1981] Minimize the Difference Between Target and Chosen Elements
#

# @lc code=start
from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        if len(mat) == 1:
            return min([abs(target - s) for s in mat[0]])
        for index, nums in enumerate(mat[1 : ]):
            possibleSum = set()
            nums1 = list(set(mat[index]))
            nums2 = list(set(mat[index - 1]))
            for i in range(len(nums1)):
                for j in range(len(nums2)):
                    possibleSum.add(nums1[i] + nums2[j])
            mat[index] = list(possibleSum)
        print(possibleSum)
        return min([abs(target - s) for s in possibleSum])
# @lc code=end


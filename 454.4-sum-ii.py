#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        nums3.sort()
        nums4.sort()

        mapNums12 = defaultdict(int)
        mapNums34 = defaultdict(int)

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                mapNums12[nums1[i] + nums2[j]] += 1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                mapNums34[nums3[i] + nums4[j]] += 1
        
        answer = 0

        for num12 in mapNums12:
            if (0 - num12) in mapNums34:
                answer += mapNums12[num12] * mapNums34[0 - num12]
        
        return answer
# @lc code=end


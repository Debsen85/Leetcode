#
# @lc app=leetcode id=1865 lang=python3
#
# [1865] Finding Pairs With a Certain Sum
#

# @lc code=start
from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.hashMap1 = {}
        self.hashMap2 = {}

        for num in nums1:
            self.hashMap1[num] = self.hashMap1.get(num, 0) + 1
        
        for num in nums2:
            self.hashMap2[num] = self.hashMap2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        value = self.nums2[index]
        self.nums2[index] += val
        self.hashMap2[value] -= 1
        self.hashMap2[value + val] = self.hashMap2.get(value + val, 0) + 1

    def count(self, tot: int) -> int:
        answer = 0
        for key in self.hashMap1:
            if tot - key in self.hashMap2:
                answer += (self.hashMap1[key] * self.hashMap2[tot - key])
        return answer


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end


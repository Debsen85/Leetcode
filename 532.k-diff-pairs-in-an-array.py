#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashMap = {}
        hashSet = set()
        answer = 0
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        for num in nums:
            a, b = num, num - k if num >= k else num + k
            if a == b:
                if hashMap[a] > 1:
                    if (a, b) not in hashSet:
                        hashSet.add((a, b))
                        answer += 1
            else:
                if b in hashMap:
                    if a > b:
                        a, b = b, a
                    if (a, b) not in hashSet:
                        hashSet.add((a, b))
                        answer += 1
        return answer    
# @lc code=end


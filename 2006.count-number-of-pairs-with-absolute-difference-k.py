#
# @lc app=leetcode id=2006 lang=python3
#
# [2006] Count Number of Pairs With Absolute Difference K
#

# @lc code=start
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hashNum = {}
        visited = set()
        for num in nums:
            hashNum[num] = hashNum.get(num, 0) + 1
        answer = 0
        for key in hashNum:
            if (key + k) in hashNum and (key, key + k) not in visited:
                answer += (hashNum[key] * hashNum[key + k])
                visited.add((key, key + k))
        return answer
# @lc code=end


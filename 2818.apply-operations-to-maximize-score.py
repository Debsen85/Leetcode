#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#

# @lc code=start
from heapq import heapify, heappop
from math import sqrt
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        length = len(nums)
        mod = 10 ** 9 + 7
        scores = []
        for num in nums:
            total = 0
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    total += 1
                while num % factor == 0:
                    num //= factor
            if num >= 2:
                total += 1
            scores.append(total)

        left = [-1] * length
        right = [length] * length

        stack = []

        for index, score in enumerate(scores):
            while stack and scores[stack[-1]] < score:
                i = stack.pop()
                right[i] = index
            if stack:
                left[index] = stack[-1]
            stack.append(index)

        maxHeap = [(-num, index) for index, num in enumerate(nums)]
        heapify(maxHeap)

        result = 1

        while k > 0:
            num, index = heappop(maxHeap)
            num = -num
            operations = (index - left[index]) * (right[index] - index)
            operations = min(k, operations)
            k -= operations
            result = (result * pow(num, operations, mod)) % mod

        return result
# @lc code=end


#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        answer = []

        for index in range(min(len(nums1), k)):
            heapq.heappush(minHeap, (nums1[index] + nums2[0], nums1[index], nums2[0], 0))      
        
        while k and minHeap:
            _, num1, num2, index = heapq.heappop(minHeap)
            answer.append((num1, num2))
            if index + 1 < len(nums2):
                heapq.heappush(minHeap, (num1 + nums2[index + 1], num1, nums2[index + 1], index + 1))    
            k -= 1
        
        return answer
# @lc code=end


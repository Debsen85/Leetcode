#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        answer = []
        maxHeap = []
        minHeap = []
        heapq.heapify(maxHeap)
        heapq.heapify(minHeap)
        L, R = 0, 0
        while R < len(nums):
            if minHeap and nums[R] > minHeap[0]:
                heapq.heappush(minHeap, nums[R])
            else:
                heapq.heappush(maxHeap, -nums[R])

            if R - L + 1 > k:
                if nums[L] <= -maxHeap[0]:
                    maxHeap.remove(-nums[L])
                    heapq.heapify(maxHeap)
                else:
                    minHeap.remove(nums[L])
                    heapq.heapify(minHeap)
                L += 1

            if len(maxHeap) > len(minHeap) + 1:
                value = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -value)
            elif len(minHeap) > len(maxHeap) + 1:
                value = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -value)     

            if R - L + 1 == k:
                if len(maxHeap) > len(minHeap):
                    answer.append(-maxHeap[0])
                elif len(maxHeap) < len(minHeap):
                    answer.append(minHeap[0])
                else:
                    answer.append((-maxHeap[0] + minHeap[0]) / 2)

            R += 1

        return answer
            
# @lc code=end


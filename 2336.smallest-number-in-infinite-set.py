#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = [num for num in range(1, 1001)]
        self.hashSet = set(self.minHeap)
        heapq.heapify(self.minHeap)

    def popSmallest(self) -> int:
        if self.hashSet and self.minHeap:
            value = heapq.heappop(self.minHeap)
            self.hashSet.remove(value)
            return value
        return -1

    def addBack(self, num: int) -> None:
        if num not in self.hashSet:
            self.hashSet.add(num)
            heapq.heappush(self.minHeap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end


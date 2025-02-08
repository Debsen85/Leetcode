#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#

# @lc code=start
import heapq


class NumberContainers:

    def __init__(self):
        self.container = {}
        self.minIndex = {}

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        if number not in self.minIndex:
            self.minIndex[number] = [index]
            heapq.heapify(self.minIndex[number])
        else:
            heapq.heappush(self.minIndex[number], index)

    def find(self, number: int) -> int:
        if number not in self.minIndex:
            return -1
        while self.minIndex[number] and self.container[self.minIndex[number][0]] != number:
            heapq.heappop(self.minIndex[number])
        return self.minIndex[number][0] if self.minIndex[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end


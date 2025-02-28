#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#

# @lc code=start
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.movingAverage = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.movingAverage) == self.size:
            self.movingAverage.popleft()
        self.movingAverage.append(val)
        return sum(self.movingAverage) / len(self.movingAverage)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end


#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque

class RecentCounter:

    def __init__(self):
        self.recentCounter = deque()

    def ping(self, t: int) -> int:
        while self.recentCounter and self.recentCounter[0] < t - 3000:
            self.recentCounter.popleft()
        self.recentCounter.append(t)
        return len(self.recentCounter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end


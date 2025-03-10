#
# @lc app=leetcode id=1756 lang=python3
#
# [1756] Design Most Recently Used Queue
#

# @lc code=start
class MRUQueue:

    def __init__(self, n: int):
        self.queue = [num for num in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        value = self.queue.pop(k - 1)
        self.queue.append(value)
        return value



# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
# @lc code=end


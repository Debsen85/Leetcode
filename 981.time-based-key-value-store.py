#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(dict)
        self.largest = defaultdict(list)

    def getTimestamp(self, nums, target):
        if len(nums) == 1:
            return nums[0]
        if nums[-1] <= target:
            return nums[-1]
        answer = nums[-1]
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] <= target:
                answer = nums[M]
                L = M + 1
            else:
                R = M - 1
        return answer

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value
        self.largest[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap or len(self.largest[key]) == 0:
            return ""
        return self.timeMap[key][self.getTimestamp(self.largest[key], timestamp)] if self.largest[key][0] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end


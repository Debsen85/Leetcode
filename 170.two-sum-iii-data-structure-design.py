#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#

# @lc code=start
from collections import defaultdict

class TwoSum:

    def __init__(self):
        self.data = defaultdict(int)

    def add(self, number: int) -> None:
        self.data[number] += 1

    def find(self, value: int) -> bool:
        for key in self.data:
            if value - key in self.data:
                if value - key == key:
                    if self.data[key] > 1:
                        return True
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end


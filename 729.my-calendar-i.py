#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class TreeNode:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = None
        self.isInserted = False

    def book(self, startTime: int, endTime: int) -> bool:
        self.isInserted = False
        self.root = self.insertValue(self.root, startTime, endTime)
        return self.isInserted

    def insertValue(self, root, startTime, endTime):
        if not root:
            self.isInserted = True
            return TreeNode(startTime, endTime)

        if endTime <= root.start:
            root.left = self.insertValue(root.left, startTime, endTime)

        if startTime >= root.end:
            root.right = self.insertValue(root.right, startTime, endTime)

        return root
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# @lc code=end


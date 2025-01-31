#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            for j in range(1, len(self.matrix[0])):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][j - 1]
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                total += self.matrix[row][col2]
            else:
                total += self.matrix[row][col2] - self.matrix[row][col1 - 1]
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


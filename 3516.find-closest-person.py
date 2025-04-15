class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 0 if (abs(x - z) == abs(y - z)) else 1 if abs(x - z) < abs(y - z) else 2
    
solution = Solution()
print(solution.findClosest(2, 4, 7))
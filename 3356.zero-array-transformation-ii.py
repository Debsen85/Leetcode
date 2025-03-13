#
# @lc app=leetcode id=3356 lang=python3
#
# [3356] Zero Array Transformation II
#

# @lc code=start
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def isZeroArray(nums, queries, mid):
            difference = [0 for _ in range(len(nums))]
            for l, r, v in queries[:mid]:
                difference[l] += v
                if r + 1 < len(nums):
                    difference[r + 1] -= v
            if difference[0] < nums[0]: return False
            for i in range(1, len(nums)):
                difference[i] += difference[i - 1]
                if difference[i] < nums[i]: return False
            return True

        left, right, ans = 0, len(queries), -1
        while left <= right:
            mid = (left + right) // 2
            if isZeroArray(nums, queries, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
# @lc code=end


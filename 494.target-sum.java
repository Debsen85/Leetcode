/*
 * @lc app=leetcode id=494 lang=java
 *
 * [494] Target Sum
 */

// @lc code=start
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for (int num: nums) sum += num;
        int [][] cache = new int[nums.length][2 * sum + 1];
        for (int i = 0; i < nums.length; i ++) {
            for (int j = 0; j <= 2 * sum; j ++) {
                cache[i][j] = Integer.MIN_VALUE;
            }
        }
        return backtracking(0, nums, target, cache, 0, sum);
    }

    public int backtracking(int index, int[] nums, int target, int[][] cache, int total, int sum) {
        if (index == nums.length) {
            if (target == total) {
                return 1;
            }
            return 0;
        }
        if (cache[index][total + sum] != Integer.MIN_VALUE) {
            return cache[index][total + sum];
        }
        cache[index][total + sum] = backtracking(index + 1, nums, target, cache, total + nums[index], sum) + backtracking(index + 1, nums, target, cache, total - nums[index], sum);
        return cache[index][total + sum];
    }
}
// @lc code=end


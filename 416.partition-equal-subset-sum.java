/*
 * @lc app=leetcode id=416 lang=java
 *
 * [416] Partition Equal Subset Sum
 */

// @lc code=start
class Solution {
    public boolean backtracking(int index, int[] nums, int total, int sum, int[][] cache) {
        if (total == sum) {
            return true;
        }
        if (index == nums.length || total > sum) {
            return false;
        }
        if (cache[index][total] != -1) {
            return cache[index][total] == 1 ? true : false;
        }
        cache[index][total] = (backtracking(index + 1, nums, total, sum, cache) || backtracking(index + 1, nums, total + nums[index], sum, cache)) == true ? 1 : 0;
        
        return cache[index][total] == 1 ? true : false;
    }

    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int num: nums) {
            sum += num;
        }
        if (sum % 2 == 1) {
            return false;
        }
        int[][] cache = new int[nums.length][sum / 2 + 1];
        for (int i = 0; i < nums.length; i ++) {
            for (int j = 0; j <= sum / 2; j ++) {
                cache[i][j] = -1;
            }
        }
        return backtracking(0, nums, 0, sum / 2, cache);
    }
}
// @lc code=end


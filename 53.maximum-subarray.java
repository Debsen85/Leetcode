/*
 * @lc app=leetcode id=53 lang=java
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int total = Integer.MIN_VALUE, currSum = 0;
        for (int num: nums) {
            if (currSum <= 0) {
                currSum = num;
            } else {
                currSum += num;
            }
            total = Math.max(total, currSum);
        }
        return total;
    }
}
// @lc code=end

